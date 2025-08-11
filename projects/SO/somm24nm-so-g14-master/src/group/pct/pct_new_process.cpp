/*
 *  \author Rafael Dias N114258
 */

#include "somm24.h"

#include <stdint.h>
#include <errno.h>
namespace group 
{

// ================================================================================== //

    uint16_t pctNewProcess(double admissionTime, double lifetime, uint32_t memSize)
    {
        soProbe(304, "%s(%0.1f, %0.1f, %#x)\n", __func__, admissionTime, lifetime, memSize);

        require(pctList != UNDEF_PCT_NODE, "Module is not in a valid open state!");
        require(admissionTime >= 0, "Bad admission time");
        require(lifetime > 0, "Bad lifetime");
        require(memSize > 0, "Bad memory size");

        /* TODO POINT: Replace next instruction with your code */
        static uint16_t nextPID = 0;


        //if (nextPID >= MAX_JOBS) {                                                              
        //    throw Exception(ENOSYS, __func__);                        // não sei qual é a exceção
        //}

        uint16_t pid = pctPID[nextPID];
        nextPID++;  

        PctNode* newNode = (PctNode*) malloc(sizeof(PctNode));
        if (newNode == NULL) {
            throw Exception(errno, __func__);                               
        }

        newNode->pcb.pid = pid;
        newNode->pcb.state = NEW;
        newNode->pcb.storeTime = UNDEF_TIME;
        newNode->pcb.startTime = UNDEF_TIME;
        newNode->pcb.finishTime = UNDEF_TIME;
        newNode->pcb.memStart = UNDEF_ADDRESS;
        newNode->pcb.memSize = memSize;
        newNode->pcb.lifetime = lifetime;
        newNode->pcb.admissionTime = admissionTime;
        newNode->next = NULL;

        
        if (pctList == NULL || pctList->pcb.pid > pid) {
            
            newNode->next = pctList;
            pctList = newNode;
        } else {
            
            PctNode* current = pctList;
            while (current->next != NULL && current->next->pcb.pid < pid) {
                current = current->next;
            }
            
            newNode->next = current->next;
            current->next = newNode;
        }

        
        return pid;
        //throw Exception(ENOSYS, __func__);
    }

// ================================================================================== //

} // end of namespace group

