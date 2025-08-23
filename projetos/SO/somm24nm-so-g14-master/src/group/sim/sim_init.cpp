/*
 *  \author Tiago Almeida - 113106; Gabriel Boia (113167)
 */

#include "somm24.h"

#include <stdio.h>

#include <sys/types.h>
#include <unistd.h>
#include <time.h>


namespace group
{

// ================================================================================== //

    void simInit(FILE *fin)
    {
        soProbe(101, "%s(%p)\n", __func__, fin);

        require(simTime == UNDEF_TIME and stepCount == UNDEF_COUNT, "Module is not in a valid closed state!");
        require(submissionTime == UNDEF_TIME and runoutTime == UNDEF_TIME, "Module is not in a valid closed state!");
        require(runningProcess == UNDEF_PID, "Module is not in a valid closed state!");
        require(fin == nullptr or fileno(fin) != -1, "fin must be NULL or a valid file pointer");

        /* TODO POINT: Replace next instruction with your code */
        //throw Exception(ENOSYS, __func__);
        SimParameters* sim = (SimParameters*)malloc(sizeof(SimParameters));
        sim->jobLoadStream = NULL;
        sim->jobMaxSize = 0x10000;
        sim->jobRandomSeed = UNDEF_SEED;
        sim->jobCount = 0;
        sim->pidStart = 1001;
        sim->pidRandomSeed = UNDEF_SEED;
        sim->memorySize = 0x100000;
        sim->memoryKernelSize = 0x10000;
        sim->memoryAllocPolicy = WorstFit;
        sim->schedulingPolicy = FCFS;
        sim->swappingPolicy = FIFO;

        jdtInit();
        
        if(fin != NULL){ 
            simConfig(fin,sim);
        }
        else{
            sim->jobRandomSeed = getpid();
            sim->pidRandomSeed = time(NULL);
        }
        
        if (sim->jobRandomSeed == UNDEF_SEED && sim->jobCount == 0 && sim->jobLoadStream != NULL){ jdtLoad(sim->jobLoadStream, sim->jobMaxSize); }
        else { jdtRandomFill(sim->jobRandomSeed, sim->jobCount, sim->jobMaxSize); }

        pctInit(sim->pidStart,jdtCount,sim->pidRandomSeed);
        rdyInit(sim->schedulingPolicy);
        swpInit(sim->swappingPolicy);
        memInit(sim->memorySize, sim->memoryKernelSize, sim->memoryAllocPolicy);

        stepCount = 0;
        simTime = 0;
        submissionTime = jdtNextSubmission();
        runoutTime = NEVER;
        runningProcess = 0;
    }

// ================================================================================== //

} // end of namespace group

