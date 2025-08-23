/*
 *  \author Rafael Dias N114258, Tiago Almeida - 113106
 */

#include "somm24.h"

#include <stdint.h>
#include <string.h>

namespace group 
{

// ================================================================================== //

    uint32_t memBiggestFreeBlockSize()
    {
        soProbe(406, "%s()\n", __func__);

        require(memAllocationPolicy != UndefMemoryAllocationPolicy, "Module is not in a valid open state!");
        require(memFreeList != UNDEF_MEM_NODE and memOccupiedList != UNDEF_MEM_NODE, "Module is not in a valid open state!");

        /* TODO POINT: Replace next instruction with my code */
        // throw Exception(ENOSYS, __func__);
        
        uint32_t biggestSize = 0;
        MemNode* current = memFreeList;

        while (current != NULL) {
            if (current->block.size > biggestSize) {
                biggestSize = current->block.size;
            }
            current = current->next;
        }

        return biggestSize;
    }

// ================================================================================== //

    uint32_t memAlloc(uint32_t size)
    {
        soProbe(404, "%s(%#x)\n", __func__, size);

        require(memAllocationPolicy != UndefMemoryAllocationPolicy, "Module is not in a valid open state!");
        require(memFreeList != UNDEF_MEM_NODE and memOccupiedList != UNDEF_MEM_NODE, "Module is not in a valid open state!");

        /* TODO POINT: Replace next instruction with my code */
        // throw Exception(ENOSYS, __func__);

        MemNode* selectedNode = NULL; // Ponteiro para o bloco selecionado

        selectedNode = memRetrieveNodeFromFreeList(size, memAllocationPolicy);

        memAddNodeToOccupiedList(selectedNode);

        return selectedNode->block.start;
    }
    

// ================================================================================== //

} // end of namespace group

