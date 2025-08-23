/*
 *  \author Rafael Dias N114258
 */

#include "somm24.h"

namespace group
{

// ================================================================================== //

    void swpTerm()
    {
        soProbe(602, "%s()\n", __func__);

        require(swappingPolicy == FIFO or swappingPolicy == FirstFit, "Module is not in a valid open state!");
        require(swpList != UNDEF_SWP_NODE and swpTail != UNDEF_SWP_NODE, "Module is not in a valid open state!");

        /* TODO POINT: Replace next instruction with your code */
        SwpNode *current = swpList;
        while (current != NULL) {
            SwpNode *nextNode = current->next; 
            free(current);  
            current = nextNode;  
        }
        swpList = UNDEF_SWP_NODE;
        swpTail = UNDEF_SWP_NODE;
        swappingPolicy = UndefSwappingPolicy;

        //throw Exception(ENOSYS, __func__);
    }

// ================================================================================== //

} // end of namespace group

