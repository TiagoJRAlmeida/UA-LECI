/*
 *  \author Gabriel Boia (113167)
 */

#include "somm24.h"

namespace group
{

// ================================================================================== //

    void rdyTerm()
    {
        soProbe(502, "%s()\n", __func__);

        require(schedulingPolicy == FCFS or schedulingPolicy == SPN, "Module is not in a valid open state!");
        require(rdyList != UNDEF_RDY_NODE and rdyTail != UNDEF_RDY_NODE, "Module is not in a valid open state!");

        /* TODO POINT: Replace next instruction with my code */
        //throw Exception(ENOSYS, __func__);

        RdyNode *current_node = rdyList;

        while (current_node != NULL){
            RdyNode *next_node = current_node->next;
            free(current_node);
            current_node = next_node; 
        }

        rdyList = UNDEF_RDY_NODE;
        rdyTail = UNDEF_RDY_NODE;

        schedulingPolicy = UndefSchedulingPolicy;
    }

// ================================================================================== //

} // end of namespace group

