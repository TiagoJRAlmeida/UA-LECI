/*
 *  \author Rafael Dias N114258
 */

#include "somm24.h"

namespace group
{

// ================================================================================== //

    void swpInsert(uint16_t pid, uint32_t size)
    {
        soProbe(604, "%s(%hu, %u)\n", __func__, pid, size);

        require(swappingPolicy == FIFO or swappingPolicy == FirstFit, "Module is not in a valid open state!");
        require(swpList != UNDEF_SWP_NODE and swpTail != UNDEF_SWP_NODE, "Module is not in a valid open state!");
        require(pid != 0, "a valid process ID must be greater than zero");

        /* TODO POINT: Replace next instruction with your code */
        SwpNode* newNode = (SwpNode*)malloc(sizeof(SwpNode));

        if (newNode == NULL) {
            throw Exception(ENOSYS, __func__);              // não sei qual a exceção atirar, vou usar as que estavam. Não encontrei na documentação
        }

        newNode -> process.pid = pid;
        newNode -> process.size = size;
        newNode -> next = NULL;

        if (swpList == NULL) {
            swpList = newNode;
            swpTail = newNode;
        }
        else {
            swpTail->next = newNode; 
            swpTail = newNode;       

        }
        //throw Exception(ENOSYS, __func__);
    }

// ================================================================================== //

} // end of namespace group

