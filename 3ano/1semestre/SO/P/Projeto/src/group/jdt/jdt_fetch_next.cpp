/*
 *  \author ...
 */

#include "somm24.h"

namespace group
{

// ================================================================================== //

    /*
     * Remove and return the oldest job description table
     */
    Job jdtFetchNext()
    {
        soProbe(207, "%s()\n", __func__);

        require(maxAddressSize != UNDEF_SIZE, "Module must be open");

        /* TODO POINT: Replace next instruction with your code */
        throw Exception(ENOSYS, __func__);
    }

// ================================================================================== //

} // end of namespace group


