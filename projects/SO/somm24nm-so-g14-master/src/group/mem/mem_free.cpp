/*
 *  \author Rafael Carvalho Dias N114258, Tiago Almeida - 113106
 */

#include "somm24.h"

#include <stdint.h>

#include <errno.h>

namespace group 
{

// ================================================================================== //

    void memFree(uint32_t address)
    {
        soProbe(405, "%s(%#x)\n", __func__, address);

        require(memAllocationPolicy != UndefMemoryAllocationPolicy, "Module is not in a valid open state!");
        require(memFreeList != UNDEF_MEM_NODE and memOccupiedList != UNDEF_MEM_NODE, "Module is not in a valid open state!");

        /* TODO POINT: Replace next instruction with my code */
        //throw Exception(ENOSYS, __func__);

        MemNode* nodeToFree = memRetrieveNodeFromOccupiedList(address);

        memAddNodeToFreeList(nodeToFree);
    }

// ================================================================================== //

} // end of namespace group

