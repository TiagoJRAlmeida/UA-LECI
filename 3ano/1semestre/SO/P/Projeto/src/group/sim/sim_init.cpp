/*
 *  \author ...
 */

#include "somm24.h"

namespace group
{

// ================================================================================== //

    /*
     * \brief Init the module's internal data structure
     */
    void simInit(SimulationParameters *spp)
    {
        soProbe(101, "%s(%p)\n", __func__, spp);

        require(simTime == UNDEF_TIME and submissionTime == UNDEF_TIME
                    and runoutTime == UNDEF_TIME, "Module is not in a valid closed state!");
        require(spp != NULL, "spp must be a valid pointer");

        /* TODO POINT: Replace next instruction with your code */
        throw Exception(ENOSYS, __func__);
    }

// ================================================================================== //

} // end of namespace group

