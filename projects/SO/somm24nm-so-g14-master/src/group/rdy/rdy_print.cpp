/*
 *  \author Tiago Costa (114629)
 */

#include "somm24.h"
#include <string.h>
#include <stdio.h>
#include <stdint.h>

namespace group 
{

// ================================================================================== //

    void rdyPrint(FILE *fout)
    {
        soProbe(503, "%s(%p)\n", __func__, fout);

        require(schedulingPolicy == FCFS || schedulingPolicy == SPN, "Module is not in a valid open state!");
        require(rdyList != UNDEF_RDY_NODE && rdyTail != UNDEF_RDY_NODE, "Module is not in a valid open state!");

        const char *policyName = (schedulingPolicy == FCFS) ? "FCFS" : "SPN";

        fprintf(fout, "+====================+\n");
        fprintf(fout, "|  RDY Module State  |\n");
        if (strcmp(policyName, "FCFS") == 0) {
            fprintf(fout, "|       (%-4s)       |\n", policyName);
        } else {
            fprintf(fout, "|       (%-3s)        |\n", policyName);
        }
        fprintf(fout, "+-------+------------+\n");
        fprintf(fout, "|  PID  |  lifetime  |\n");
        fprintf(fout, "+-------+------------+\n");

        
        RdyNode *current = rdyList; 
        while (current != NULL) {
            fprintf(fout, "| %5d | %10.1f |\n", current->process.pid, current->process.lifetime);
            current = current->next;
        }

        fprintf(fout, "+====================+\n");
    }
// ================================================================================== //

} // end of namespace group

