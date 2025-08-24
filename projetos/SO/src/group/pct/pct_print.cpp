/*
 *  \author Rafael Carvalho Dias N 114258
 */

#include "somm24.h"

#include <stdio.h>
#include <stdint.h>

namespace group 
{

// ================================================================================== //

    void pctPrint(FILE *fout)
    {
        soProbe(303, "%s(%p)\n", __func__, fout);

        require(pctList != UNDEF_PCT_NODE, "Module is not in a valid open state!");
        require(fout != NULL and fileno(fout) != -1, "fout must be a valid file stream");

        /* TODO POINT: Replace next instruction with your code */
        fprintf(fout, "+======================================================================================================================+\n");
        fprintf(fout, "|                                                   PCT module state                                                   |\n");
        fprintf(fout, "+-------+-------------+-------------+-------------+------------+------------+-------------+--------------+-------------+\n");
        fprintf(fout, "|  PID  |    state    |  admission  |  lifetime   | store time | start time | finish time | memory start | memory size |\n");
        fprintf(fout, "+-------+-------------+-------------+-------------+------------+------------+-------------+--------------+-------------+\n");

        PctNode* current = pctList;

        while (current != NULL) {
            const char* state = 
                (current->pcb.state == NEW) ? "NEW" :
                (current->pcb.state == RUNNING) ? "RUNNING" :
                (current->pcb.state == READY) ? "READY" :
                (current->pcb.state == SWAPPED) ? "SWAPPED" :
                (current->pcb.state == TERMINATED) ? "TERMINATED" : "UNKNOWN";


            fprintf(fout, "| %5u | %-11s | %11.1f | %11.1f |", 
                current->pcb.pid,                      
                state,                                  
                current->pcb.admissionTime,            
                current->pcb.lifetime);                 


            if (current->pcb.state == SWAPPED) {
                fprintf(fout, "  %9s |", "UNDEF");  
            } else {
                fprintf(fout, " %10.1f |", current->pcb.storeTime);  
            }


            if (current->pcb.startTime == UNDEF_TIME) {
                fprintf(fout, " %10s |", "UNDEF");
            } else {
                fprintf(fout, " %10.1f |", current->pcb.startTime);  
            }

 
            if (current->pcb.finishTime == UNDEF_TIME) {
                fprintf(fout, " %11s |", "UNDEF");
            } else {
                fprintf(fout, " %11.1f |", current->pcb.finishTime);  
            }


            if (current->pcb.state == SWAPPED) {
                fprintf(fout, "   %10s |      0x%-4x |\n", "UNDEF", current->pcb.memSize);  
            } else {

                int memStartWidth = snprintf(NULL, 0, "%x", current->pcb.memStart); 
                int memSizeWidth = snprintf(NULL, 0, "%x", current->pcb.memSize);   

                fprintf(fout, "     %*s0x%-*x |    %*s0x%-*x |\n",
                    6 - memStartWidth, "", memStartWidth, current->pcb.memStart, 
                    6 - memSizeWidth, "", memSizeWidth, current->pcb.memSize);   
            }
            current = current->next;
        }

        fprintf(fout, "+======================================================================================================================+\n");
    }

// ================================================================================== //

} // end of namespace group

