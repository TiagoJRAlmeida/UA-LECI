/*
 *  \author Rafael Dias N114258
 */

#include "somm24.h"

namespace group 
{

// ================================================================================== //

    void pctInit(uint16_t pid0, uint16_t cnt, uint32_t seed) 
    {
        soProbe(301, "%s(%hu, %hu, %u)\n", __func__, pid0, cnt, seed);

        require(pctList == UNDEF_PCT_NODE, "The module is not in a valid closed state");
        require(cnt > 1 and cnt <= MAX_JOBS, "cnt must be > 1 and <= MAX_JOBS");
        
        /* TODO POINT: Replace next instruction with your code */
        pctList = NULL;

        srand(seed); 

        uint16_t pidArray[MAX_JOBS];

        for (uint16_t i = 0; i < cnt; i++) {
            pidArray[i] = pid0 + i;
        }

        for (uint16_t i = cnt - 1; i > 0; i--) {
            uint16_t j = rand() % (i + 1);

            uint16_t temp = pidArray[i];
            pidArray[i] = pidArray[j];
            pidArray[j] = temp;
        }

        for (uint16_t i = 0; i < cnt; i++) {
            pctPID[i] = pidArray[i];
        }

        for (uint16_t i = cnt; i < MAX_JOBS; i++) {
            pctPID[i] = 0;
        }
    }

// ================================================================================== //

} // end of namespace group

