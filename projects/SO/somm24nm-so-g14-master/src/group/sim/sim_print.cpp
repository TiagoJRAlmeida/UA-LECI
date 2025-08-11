/*
 *  \author Tiago Costa (114629)
 */

#include "somm24.h"

#include <stdio.h>
#include <stdint.h>

namespace group 
{

// ================================================================================== //

void simPrint(FILE *fout, uint32_t satelliteModules) {
    soProbe(103, "%s(\"%p\")\n", __func__, fout);

    // Ensure the SIM module is in a valid open state
    require(simTime != UNDEF_TIME && stepCount != UNDEF_COUNT, "Module not in a valid open state!");
    require(submissionTime != UNDEF_TIME && runoutTime != UNDEF_TIME, "Module is not in a valid open state!");
    require(runningProcess != UNDEF_PID, "Module is not in a valid open state!");
    require(fout != NULL && fileno(fout) != -1, "fout must be a valid file stream");


    if (satelliteModules & PRINT_JDT) {
        jdtPrint(fout);
        fprintf(fout, "\n");
    }
    if (satelliteModules & PRINT_PCT) {
        pctPrint(fout);
        fprintf(fout, "\n");
    }
    if (satelliteModules & PRINT_MEM) {
        memPrint(fout);
        fprintf(fout, "\n");
    }
    if (satelliteModules & PRINT_RDY) {
        rdyPrint(fout);
        fprintf(fout, "\n");
    }
    if (satelliteModules & PRINT_SWP) {
        swpPrint(fout);
        fprintf(fout, "\n");
    }

    fprintf(fout, "+====================================================================================+\n");
    fprintf(fout, "+ -------------------------------- SIM Module State -------------------------------- +\n");
    fprintf(fout, "+====================================================================================+\n");
    fprintf(fout, "| simulation time |  step count  | running process | next submission |  next runout  |\n");
    fprintf(fout, "+-----------------+--------------+-----------------+-----------------+---------------+\n");

    fprintf(fout, "| %15.1f | %12d | ", simTime, stepCount);
    if (runningProcess == 0) {
        fprintf(fout, "            --- | ");
    } else {
        fprintf(fout, "  %13d | ", runningProcess);
    }
    if (submissionTime == INFINITY) {
        fprintf(fout, "          NEVER | ");
    } else { fprintf(fout, "%15.1f | ", submissionTime); }
    if (runoutTime == INFINITY) {
        fprintf(fout, "        NEVER |\n");
    } else {
        fprintf(fout, "%13.1f |\n", runoutTime);
    }

    fprintf(fout, "+====================================================================================+\n");

}

// ================================================================================== //

} // end of namespace group

