/*
 *  \author ...
 */

#include "somm24.h"

namespace group
{

// ================================================================================== //

    bool simStep()
    {
        soProbe(104, "%s()\n", __func__);

        require(simTime != UNDEF_TIME and submissionTime != UNDEF_TIME, "Module not in a valid open state!");

        /* TODO POINT: Replace next instruction with your code */
        throw Exception(ENOSYS, __func__);
    }

// ================================================================================== //

} // end of namespace group

