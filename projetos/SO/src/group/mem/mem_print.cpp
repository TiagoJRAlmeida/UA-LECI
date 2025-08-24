/*
 *  \author Tiago Almeida - 113106
 */

#include "somm24.h"

#include <stdio.h>
#include <stdint.h>

namespace group 
{

// ================================================================================== //

    void memPrint(FILE *fout)
    {
        soProbe(403, "%s(\"%p\")\n", __func__, fout);

        require(memAllocationPolicy != UndefMemoryAllocationPolicy, "Module is not in a valid open state!");
        require(memFreeList != UNDEF_MEM_NODE and memOccupiedList != UNDEF_MEM_NODE, "Module is not in a valid open state!");
        require(fout != NULL and fileno(fout) != -1, "fout must be a valid file stream");

        /* TODO POINT: Replace next instruction with my code */
        // throw Exception(ENOSYS, __func__);

        MemNode* currentNode;

        // Print header
        fprintf(fout, "+===============================+\n");
        fprintf(fout, "|       MEM module state        |\n");
        if(memAllocationPolicy == BestFit){
            fprintf(fout, "|           (BestFit)           |\n");
        } else{
            fprintf(fout, "|          (WorstFit)           |\n");
        }

        // Print occupied list
        fprintf(fout, "+-------------------------------+\n");
        fprintf(fout, "|         occupied list         |\n");
        fprintf(fout, "+---------------+---------------+\n");
        fprintf(fout, "|  start frame  |     size      |\n");
        fprintf(fout, "+---------------+---------------+\n");
        currentNode = memOccupiedList;
        while(currentNode != NULL){
            int memStartWidth = snprintf(NULL, 0, "%x", currentNode->block.start); 
            int memSizeWidth = snprintf(NULL, 0, "%x", currentNode->block.size);   

            fprintf(fout, "|      %*s0x%-*x |      %*s0x%-*x |\n",
                6 - memStartWidth, "", memStartWidth, currentNode->block.start, 
                6 - memSizeWidth, "", memSizeWidth, currentNode->block.size); 
            currentNode = currentNode->next; 
        }

        // Print free list
        fprintf(fout, "+---------------+---------------+\n");
        fprintf(fout, "|            free list          |\n");
        fprintf(fout, "+---------------+---------------+\n");
        fprintf(fout, "|  start frame  |     size      |\n");
        fprintf(fout, "+---------------+---------------+\n");
        currentNode = memFreeList;
        while(currentNode != NULL){
            int memStartWidth = snprintf(NULL, 0, "%x", currentNode->block.start); 
            int memSizeWidth = snprintf(NULL, 0, "%x", currentNode->block.size);   

            fprintf(fout, "|      %*s0x%-*x |      %*s0x%-*x |\n",
                6 - memStartWidth, "", memStartWidth, currentNode->block.start, 
                6 - memSizeWidth, "", memSizeWidth, currentNode->block.size); 
            currentNode = currentNode->next; 
        }
        fprintf(fout, "+===============================+\n");
    }

// ================================================================================== //

} // end of namespace group

