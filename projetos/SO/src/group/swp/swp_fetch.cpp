/*
 *  \author Rafael Dias N114258
 */

#include "somm24.h"

namespace group
{

// ================================================================================== //

    uint16_t swpFetch(uint32_t sizeAvailable)
    {
        soProbe(605, "%s(%#x)\n", __func__, sizeAvailable);

        require(swappingPolicy == FIFO or swappingPolicy == FirstFit, "Module is not in a valid open state!");
        require(swpList != UNDEF_SWP_NODE and swpTail != UNDEF_SWP_NODE, "Module is not in a valid open state!");

        /* TODO POINT: Replace next instruction with your code */
        if (swpList == NULL) {
            return 0; 
        }
        if (swappingPolicy == FIFO) {

            if (swpList -> process.size <= sizeAvailable) {

                uint16_t pid = swpList -> process.pid;
                swpList = swpList -> next;
                return pid;

            } else {

                return 0;

            }
        } else if (swappingPolicy == FirstFit) {

            SwpNode* current = swpList;
            SwpNode* previous = NULL;

            while (current != NULL) {

                if (current->process.size <= sizeAvailable) {

                    uint16_t pid = current->process.pid;  

                    if (previous != NULL) {

                        previous->next = current->next;  

                    } else {

                        swpList = current->next;  
                    }

                    return pid;  
                }

                previous = current;
                current = current->next;
            }

            return 0;
        } else {
            throw Exception(EINVAL, __func__);
        }
        // throw Exception(ENOSYS, __func__);
    }

// ================================================================================== //

} // end of namespace group

