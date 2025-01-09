/*
 *  
 *  ...
 *
 *  \author Artur Pereira - 2024
 */

#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <libgen.h>
#include <termios.h>
#include <regex.h>

#include <string>
#include <iostream>
#include <map>

#include "somm24.h"


/* ******************************************** */
/* print help message */
static void printUsage(const char *cmd_name, const SimulationParameters *spp)
{
    uint32_t jmm = spp->jobMaximumMemory;
    MemoryAllocationPolicy map = spp->memoryAllocPolicy;
    const char *mas = map == BestFit ? "bf" : "wf";
    uint32_t ms = spp->memorySize;
    uint32_t mks = spp->memoryKernelSize;
    SwappingPolicy sp = spp->swappingPolicy;
    const char *sp_as = sp == FirstProcess ? "fp" : "ffp";
    SchedulingPolicy psp = spp->schedulingPolicy;
    const char *psp_as = psp == FCFS ? "FCFS" : "SPN";
    printf("Sinopsis: %s [OPTIONS]\n"
           "  OPTIONS:\n"
           "  -i infile      --- job input file (default: none)\n"
           "  -o outfile     --- print output file (default: stdout)\n"
           "  -j [0x]num     --- maximum number of frames a job may request (default: %#x or %u)\n"
           "  -f wf|bf       --- memory allocation policy (one of wf [WorstFit] or bf [BestFit]; default: %s)\n"
           "  -m [0x]num     --- total number of frames the main memory comprises (default: %#x or %u)\n"
           "  -k [0x]num     --- number of frames the kernel uses (default: %#x or %u)\n"
           "  -s fp|ffp      --- swapping policy (one of fp [FirstProcess] or ffp [FirstFitProcess]; default: %s)\n"
           "  -p fcfs|spn    --- processor scheduling policy (one of FCFS or SPN; default: %s)\n"
           "  -O outfile     --- probbing file (default: stdout)\n"
           "  -P num-num     --- probe ID range (default: 0-0)\n"
           "  -A num[-num]   --- add ID or range of IDs to probe configuration\n"
           "  -R num[-num]   --- remove ID or range of IDs from probe configuration\n"
           "  -b             --- set bin selection map to 100-699\n"
           "  -g             --- set bin selection map to 0-0 (default)\n"
           "  -a num[-num]   --- add ID or range of IDs to bin selection map\n"
           "  -r num[-num]   --- remove ID or range of IDs from bin selection map\n"
           "  -S             --- run in single step\n"
           "  -h             --- print this help\n", cmd_name,
           jmm, jmm, mas, ms, ms, mks, mks, sp_as, psp_as
    );
}

/* ******************************************** */
/*
 * pause simulation
 */
bool pauseSim(const char *prompt = "", bool quit = true)
{
    static bool firstTime = true;
    static struct termios prev, cur;
    if (firstTime)
    {
        firstTime = false;
        tcgetattr(STDIN_FILENO, &prev);
        cur = prev;
        cur.c_lflag &= (~ICANON);
        tcsetattr(STDIN_FILENO, TCSANOW, &cur);
    }

    printf("%s. Continue (Y/n)? ", prompt); fflush(stdout);
    int res;
    while (true)
    {
        res = getchar();
        printf("\n");
        if (res == 'n' or res == 'N') break;
        if (res == 'y' or res == 'Y' or res == '\n') return true;
        printf("Bad option! Continue (Y/n)? "); fflush(stdout);
    }
    if (quit) exit(0);
    else return false;
}

/* ******************************************** */
/* The main function */
int main(int argc, char *argv[])
{
    const char *progName = basename(argv[0]); 

    /* by default, send probing to stdout */
    soProbeOpen(stdout, 0, 0);

    /* module print stream */
    FILE *fout = stdout;

    /* single step execution */
    bool singleStep = false;

    /* set default simulation parameters */
    SimulationParameters simulationParameters = {
        .jobMaximumMemory = 1 << 15,
        .jobLoadStream = nullptr,
        .jobCount = 0,
        .jobRandomSeed = 0,
        .memorySize = 1 << 20,
        .memoryKernelSize = 1 << 15,
        .memoryAllocPolicy = WorstFit,
        .schedulingPolicy = FCFS,
        .swappingPolicy = FirstProcess
    };

    /* process command line options */
    int opt;
    while ((opt = getopt(argc, argv, "i:o:j:f:m:k:p:s:O:P:A:R:bga:r:hS")) != -1)
    {
        switch (opt)
        {
            case 'i':   // --job-load-file
            {
                FILE * fin = fopen(optarg, "r");
                if (fin == nullptr)
                {
                    fprintf(stderr, "%s: Bad argument (\"%s\"): fail opening file.\n", progName, optarg);
                    return EXIT_FAILURE;
                }
                simulationParameters.jobLoadStream = fin;
                break;
            }
            case 'o':   // print output file // TODO point: include in simulation parameters
            {
                if ((fout = fopen(optarg, "w")) == NULL)
                {
                    fprintf(stderr, "%s: Bad argument (\"%s\"): fail opening file.\n", progName, optarg);
                    return EXIT_FAILURE;
                }
                break;
            }
            case 'j':   // maximum memory size used by a job
            {
                uint32_t jmms;
                int n = 0;
                sscanf(optarg, "%u%n", &jmms, &n);
                if ((size_t)n == strlen(optarg)) break;
                n = 0;
                sscanf(optarg, "%x%n", &jmms, &n);
                if ((size_t)n != strlen(optarg))
                {
                    fprintf(stderr, "%s: Bad argument (%s) to '-%c' option.\n", progName, optarg, opt);
                    return EXIT_FAILURE;
                }
                simulationParameters.jobMaximumMemory = jmms;
                break;
            }
            case 'f':   // memory allocation policy
            {
                MemoryAllocationPolicy map;
                if (strcasecmp(optarg, "bf") == 0) map = BestFit;
                else if (strcasecmp(optarg, "wf") == 0) map = WorstFit;
                else
                {
                    fprintf(stderr, "%s: Bad argument (%s) to '-%c' option.\n", progName, optarg, opt);
                    return EXIT_FAILURE;
                }
                simulationParameters.memoryAllocPolicy = map;
                break;
            }
            case 'm':   // memory size
            {
                uint32_t ms;
                int n = 0;
                sscanf(optarg, "%u%n", &ms, &n);
                if ((size_t)n == strlen(optarg)) break;
                n = 0;
                sscanf(optarg, "%x%n", &ms, &n);
                if ((size_t)n != strlen(optarg))
                {
                    fprintf(stderr, "%s: Bad argument (%s) to '-%c' option.\n", progName, optarg, opt);
                    return EXIT_FAILURE;
                }
                simulationParameters.memorySize = ms;
                break;
            }
            case 'k':   // memory size used by kernel
            {
                uint32_t mks;
                int n = 0;
                sscanf(optarg, "%u%n", &mks, &n);
                if ((size_t)n == strlen(optarg)) break;
                n = 0;
                sscanf(optarg, "%x%n", &mks, &n);
                if ((size_t)n != strlen(optarg))
                {
                    fprintf(stderr, "%s: Bad argument (%s) to '-%c' option.\n", progName, optarg, opt);
                    return EXIT_FAILURE;
                }
                simulationParameters.memoryKernelSize = mks;
                break;
            }
            case 's':   // swapping in policy
            {
                SwappingPolicy sp;
                if (strcasecmp(optarg, "fp") == 0) sp = FirstProcess;
                else if (strcasecmp(optarg, "ffp") == 0) sp = FirstFitProcess;
                else
                {
                    fprintf(stderr, "%s: Bad argument (%s) to '-%c' option.\n", progName, optarg, opt);
                    return EXIT_FAILURE;
                }
                simulationParameters.swappingPolicy = sp;
                break;
            }
            case 'p':   // processor scheduling policy
            {
                SchedulingPolicy sp;
                if (strcasecmp(optarg, "fcfs") == 0) sp = FCFS;
                else if (strcasecmp(optarg, "spn") == 0) sp = SPN;
                else
                {
                    fprintf(stderr, "%s: Bad argument (%s) to '-%c' option.\n", progName, optarg, opt);
                    return EXIT_FAILURE;
                }
                simulationParameters.schedulingPolicy = sp;
                break;
            }
            case 'O':          /* set probbing file */
            {
                soProbeFile(optarg);
                break;
            }
            case 'P':          /* set ID range to probing system */
            {
                uint32_t lower, upper;
                uint32_t cnt = 0;
                if ( (sscanf(optarg, "%d%*[,-]%d %n", &lower, &upper, &cnt) != 2) 
                        or (cnt != strlen(optarg)) )
                {
                    fprintf(stderr, "%s: Bad argument (%s) to '-%c' option.\n", progName, optarg, opt);
                    printUsage(progName, &simulationParameters);
                    return EXIT_FAILURE;
                }
                soProbeSetIDs(lower, upper);
                break;
            }
            case 'A':          /* add IDs to probe conf */
            {
                uint32_t lower, upper;
                uint32_t cnt = 0;
                if ( (sscanf(optarg, "%d%*[,-]%d %n", &lower, &upper, &cnt) != 2) 
                        or (cnt != strlen(optarg)) )
                {
                    fprintf(stderr, "%s: Bad argument (%s) to '-%c' option.\n", progName, optarg, opt);
                    printUsage(progName, &simulationParameters);
                    return EXIT_FAILURE;
                }
                soProbeAddIDs(lower, upper);
                break;
            }
            case 'R':          /* remove IDs from probe conf */
            {
                uint32_t lower, upper;
                uint32_t cnt = 0;
                if ( (sscanf(optarg, "%d-%d %n", &lower, &upper, &cnt) != 2) 
                        or (cnt != strlen(optarg)) )
                {
                    fprintf(stderr, "%s: Bad argument (%s) to '-%c' option.\n", progName, optarg, opt);
                    printUsage(progName, &simulationParameters);
                    return EXIT_FAILURE;
                }
                soProbeRemoveIDs(lower, upper);
                break;
            }
            case 'b':  // set binary mode
            {
                soBinSetIDs(100, 999);
                break;
            }
            case 'g':  // set binary mode
            {
                soBinSetIDs(0, 0);
                break;
            }
            case 'a':          /* add IDs to probe conf */
            case 'r':          /* remove IDs from probe conf */
            {
                regex_t regex;
                regcomp(&regex, "^[0-9]+-[0-9]+$", REG_EXTENDED | REG_NOSUB);
                uint32_t lower, upper;
                uint32_t cnt = 0;
                if (regexec(&regex, optarg, 0, NULL, 0) == 0)
                {
                    sscanf(optarg, "%u-%u", &lower, &upper);
                }
                else if ( (sscanf(optarg, "%d%n", &lower, &cnt) == 1) and (cnt == strlen(optarg)) )
                {
                    upper = lower;
                }
                else
                {
                    fprintf(stderr, "%s: Bad argument (%s) to '-%c' option.\n", progName, optarg, opt);
                    return EXIT_FAILURE;
                }
                
                if (opt == 'r')
                    soBinRemoveIDs(lower, upper);
                else
                    soBinAddIDs(lower, upper);

                break;
            }
            case 'h':
            {
                printUsage(progName, &simulationParameters);
                return 0;
            }
            case 'S':
            {
                singleStep = true;
                break;
            }
            default:
            {
                fprintf(stderr, "%s: Wrong option (\"-%c\".\n", progName, opt);
                printUsage(progName, &simulationParameters);
                return EXIT_FAILURE;
            }
        }
    }

    /* set fout stream as no buffered */
    setvbuf(fout, NULL, _IONBF, 0);

    /* init simulation */
    fprintf(stdout, "\n\e[34;1mStarting simulation\e[0m\n");

    simInit(&simulationParameters);

    /* do simulation */
    do {
        fprintf(fout, "\n//////////////////////////////////////////////////////////////\n\n");
        simPrint(fout, PRINT_ALL);
        fprintf(fout, "\n//////////////////////////////////////////////////////////////\n\n");
        if (singleStep) pauseSim();
    } while (simStep());

    /* end simulation */
    fprintf(stdout, "\n\e[34;1mEnding simulation\e[0m\n");
    simTerm();
}
