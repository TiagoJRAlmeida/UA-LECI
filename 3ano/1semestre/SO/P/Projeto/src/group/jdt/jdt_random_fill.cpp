/*
 *  \author ...
 */

#include "somm24.h"

namespace group
{

// ================================================================================== //

    uint32_t jdtRandomFill(uint32_t n, uint32_t seed)
    {
        soProbe(205, "%s(%u, %u)\n", __func__, n, seed);

        require(maxAddressSize != UNDEF_SIZE, "Module must be open");
        require(n >= 2, "At least 2 jobs are required");
        require(n <= MAX_JOBS, "More than MAX_JOBS jobs not allowed");

        /* TODO POINT: Replace next instruction with your code */
        throw Exception(ENOSYS, __func__);
    }

// ================================================================================== //

} // end of namespace group

