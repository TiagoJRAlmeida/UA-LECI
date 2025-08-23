/*
 *  \author Tiago Costa (114629)
 */

#include "somm24.h"

#include <stdio.h>
#include <stdint.h>

namespace group 
{

// ================================================================================== //

    void jdtPrint(FILE *fout)
    {
        soProbe(203, "%s(%p)\n", __func__, fout);

        require(jdtIn != UNDEF_JOB_INDEX && jdtOut != UNDEF_JOB_INDEX, "Module is not in a valid open state!");
        require(jdtCount != UNDEF_JOB_COUNT, "Module is not in a valid open state!");
        require(fout != NULL && fileno(fout) != -1, "fout must be a valid file stream");

        fprintf(fout, "+=====================================+\n");
        fprintf(fout, "|          JDT module state           |\n");
        fprintf(fout, "+------------+------------+-----------+\n");
        fprintf(fout, "| submission |  lifetime  |  memory   |\n");
        fprintf(fout, "|    time    |            | requested |\n");
        fprintf(fout, "+------------+------------+-----------+\n");

        int index = jdtOut;
        for (int count = 0; count < jdtCount; count++) {
            if (jdtTable[index].submissionTime != 0) {
                int memSizeWidth = snprintf(NULL, 0, "%x", jdtTable[index].memSize);
                fprintf(fout, "| %10.1f | %10.1f |   %*s0x%-*x |\n",
                        jdtTable[index].submissionTime,
                        jdtTable[index].lifetime,
                        5 - memSizeWidth, "", memSizeWidth, (unsigned int)jdtTable[index].memSize);
            }

            
            index = (index + 1) % MAX_JOBS;
        }

        fprintf(fout, "+=====================================+\n");
    }

// ================================================================================== //

} // end of namespace group

