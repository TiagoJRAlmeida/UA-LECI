/*
 *  \author Rafael Dias N114258, Tiago Almeida - 113106
 */

#include "somm24.h"

namespace group 
{

// ================================================================================== //

    void memTerm() 
    {
        soProbe(402, "%s()\n", __func__);

        require(memAllocationPolicy != UndefMemoryAllocationPolicy, "Module is not in a valid open state!");
        require(memFreeList != UNDEF_MEM_NODE and memOccupiedList != UNDEF_MEM_NODE, "Module is not in a valid open state!");

        /* TODO POINT: Replace next instruction with my code */
        //throw Exception(ENOSYS, __func__);

        MemNode *currentFree = memFreeList;
        while (currentFree != NULL) {
            MemNode *nextNode = currentFree->next;  
            free(currentFree);  
            currentFree = nextNode;  
        }

        MemNode *currentOccupied = memOccupiedList;
        while (currentOccupied != NULL) {
            MemNode *nextNode = currentOccupied->next; 
            free(currentOccupied);  
            currentOccupied = nextNode;  
        }

        memAllocationPolicy = UndefMemoryAllocationPolicy;
        memFreeList = UNDEF_MEM_NODE;
        memOccupiedList = UNDEF_MEM_NODE;
    }
    

// ================================================================================== //

} // end of namespace group

