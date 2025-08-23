/*
 *  \author Gabriel Boia (113167)
 */

#include "somm24.h"

namespace group 
{

// ================================================================================== //

    void simTerm() 
    {
        soProbe(102, "%s()\n", __func__);

        require(simTime != UNDEF_TIME and stepCount != UNDEF_COUNT, "Module not in a valid open state!");
        require(submissionTime != UNDEF_TIME and runoutTime != UNDEF_TIME, "Module is not in a valid open state!");
        require(runningProcess != UNDEF_PID, "Module is not in a valid open state!");

        /* TODO POINT: Replace next instruction with your code */
        //throw Exception(ENOSYS, __func__);
        stepCount = UNDEF_COUNT;
        simTime = UNDEF_TIME;
        submissionTime = UNDEF_TIME;
        runoutTime = UNDEF_TIME;
        runningProcess = UNDEF_PID;

        pctTerm();
        rdyTerm();
        swpTerm();
        memTerm();
        jdtTerm();
    }

// ================================================================================== //

} // end of namespace group

