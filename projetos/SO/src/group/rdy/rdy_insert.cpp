/*
 *  \author Gabriel Boia (113167)
 */

#include "somm24.h"

namespace group
{

// ================================================================================== //

    void rdyInsert(uint16_t pid, double lifetime)
    {
        soProbe(504, "%s(%hu, %.1f)\n", __func__, pid, lifetime);

        require(schedulingPolicy == FCFS or schedulingPolicy == SPN, "Module is not in a valid open state!");
        require(rdyList != UNDEF_RDY_NODE and rdyTail != UNDEF_RDY_NODE, "Module is not in a valid open state!");
        require(pid != 0, "a valid process ID must be greater than zero");
        require(lifetime > 0, "a valid process lifetime must be greater than zero");

        /* TODO POINT: Replace next instruction with my code */
        //throw Exception(ENOSYS, __func__);

        RdyNode *new_node = (RdyNode *)malloc(sizeof(RdyNode));
        if (new_node == NULL)
        {
            throw Exception(EINVAL, __func__);
        }
        new_node->process.pid = pid;
        new_node->process.lifetime = lifetime;
        new_node->next = NULL;

        switch (schedulingPolicy)
        {
        case FCFS:

            if (rdyList == NULL)
            {
                rdyList = new_node;
                rdyTail = new_node;
            }
            else
            {
                rdyTail->next = new_node;
                rdyTail = new_node;
            }
            break;

        case SPN:

            if (rdyList == NULL)
            {

                rdyList = new_node;
                rdyTail = new_node;
            }
            else if (lifetime < rdyList->process.lifetime)
            {

                new_node->next = rdyList;
                rdyList = new_node;
            }
            else
            {

                RdyNode *current = rdyList;
                while (current->next != NULL && current->next->process.lifetime <= lifetime)
                {
                    current = current->next;
                }

                new_node->next = current->next;
                current->next = new_node;

                if (new_node->next == NULL)
                {

                    rdyTail = new_node;
                }
            }
            break;

        default:
            throw Exception(EINVAL, __func__);
        }
    }

// ================================================================================== //

} // end of namespace group

