/*
 *  \author Tiago Costa (114629) Rafael Carvalho Dias N114258
 */

#include "somm24.h"
#include <string.h>
#include <stdio.h>
#include <stdint.h>

namespace group 
{

// ================================================================================== //

    void swpPrint(FILE *fout)
    {
        soProbe(603, "%s(%p)\n", __func__, fout);

        require(swappingPolicy == FIFO or swappingPolicy == FirstFit, "Module is not in a valid open state!");
        require(swpList != UNDEF_SWP_NODE and swpTail != UNDEF_SWP_NODE, "Module is not in a valid open state!");
        require(fout != NULL and fileno(fout) != -1, "fout must be a valid file stream");

        const char *policyName = (swappingPolicy == FIFO) ? "FIFO" : "FirstFit";
        /* TODO POINT: Replace next instruction with your code */
        fprintf(fout, "+=====================+\n");
        fprintf(fout, "|  SWP Module State   |\n");
                if (strcmp(policyName, "FIFO") == 0) {
            fprintf(fout, "|       (%-4s)        |\n", policyName);
        } else {
            fprintf(fout, "|     (%-8s)      |\n", policyName);
        }
        fprintf(fout, "+-------+-------------+\n");
        fprintf(fout, "|  PID  | memory size |\n");
        fprintf(fout, "+-------+-------------+\n");
        SwpNode* current = swpList;
        while (current != NULL) {
            int hexWidth = snprintf(NULL, 0, "%X", current->process.size);

            int padding = 6 - hexWidth;


            fprintf(fout, "| %5u |    %*s0x%x |\n", current->process.pid, padding, "", current->process.size);
            current = current->next;
        }
        fprintf(fout, "+=====================+\n");

        //throw Exception(ENOSYS, __func__);
    }

// ================================================================================== //

} // end of namespace group

