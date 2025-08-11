/*
 *  \author Gabriel Boia (113167)
 */

#include "somm24.h"

namespace group
{

// ================================================================================== //

    void simRun(uint32_t cnt)
    {
        soProbe(106, "%s(%u)\n", __func__, cnt);

        require(simTime != UNDEF_TIME and stepCount != UNDEF_COUNT, "Module not in a valid open state!");
        require(submissionTime != UNDEF_TIME and runoutTime != UNDEF_TIME, "Module is not in a valid open state!");
        require(runningProcess != UNDEF_PID, "Module is not in a valid open state!");

        /* TODO POINT: Replace next instruction with your code */
        //throw Exception(ENOSYS, __func__);

        if(cnt == 0){
            while(simStep());
        }else{
            for(uint32_t i = 0;i<cnt;i++){
                int result = simStep();
                if(!result){break;}
            }
        }
    }

// ================================================================================== //

} // end of namespace group

