/*
 *  \author Rafael Dias N114258, Tiago Almeida - 113106
 */

#include "somm24.h"

#include <stdint.h>
#include <math.h>
#include <errno.h>

namespace group 
{

// ================================================================================== //

    void memInit(uint32_t memSize, uint32_t memKernelSize, MemoryAllocationPolicy policy)
    {
        const char *pas;
        switch (policy)
        {
            case UndefMemoryAllocationPolicy: pas = "UndefMemoryAllocationPolicy"; break;
            case BestFit: pas = "BestFit"; break;
            case WorstFit: pas = "WorstFit"; break;
            default: pas = "InvalidPattern"; break;
        }
        soProbe(401, "%s(%#x, %#x, %s)\n", __func__, memSize, memKernelSize, pas);

        require(memAllocationPolicy == UndefMemoryAllocationPolicy, "Module is not in a valid closed state!");
        require(memFreeList == UNDEF_MEM_NODE and memOccupiedList == UNDEF_MEM_NODE, "Module is not in a valid closed state!");
        require(memSize > memKernelSize, "total memory size must be bigger than the one use by the kernel of OS");
        require(policy == BestFit or policy == WorstFit, "policy must be BestFit or WorstFit");

        /* TODO POINT: Replace next instruction with my code */
        // throw Exception(ENOSYS, __func__);

        memAllocationPolicy = policy;

        memFreeList = NULL;
        memOccupiedList = NULL;

        MemNode *freeNode = (MemNode*) malloc(sizeof(MemNode));  
        if (freeNode == NULL) {
            throw Exception(errno, __func__);
        }

        freeNode->block.size = memSize - memKernelSize;
        freeNode->block.start = memKernelSize;
        freeNode->next = NULL;        

        memFreeList = freeNode;
    }

// ================================================================================== //

} // end of namespace group

