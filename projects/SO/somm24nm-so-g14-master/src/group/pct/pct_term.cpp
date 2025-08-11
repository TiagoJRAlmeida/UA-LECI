/*
 *  \author Rafael Dias N114258
 */

#include "somm24.h"

namespace group 
{

// ================================================================================== //

    void pctTerm() 
    {
        soProbe(302, "%s()\n", __func__);

        require(pctList != UNDEF_PCT_NODE, "Module is not in a valid open state!");
        
        /* TODO POINT: Replace next instruction with your code */
        //throw Exception(ENOSYS, __func__);
        PctNode *current = pctList;  
        while (current != NULL) {
            PctNode *nextNode = current->next; 
            free(current);  
            current = nextNode;  
        }

        pctList = UNDEF_PCT_NODE;

        for (uint16_t i = 0; i < MAX_JOBS; i++) {
            pctPID[i] = 0;
        }
    }

// ================================================================================== //

} // end of namespace group

