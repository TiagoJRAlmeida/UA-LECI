/*
 *  \author Guilherme Matos - 114252
 */

#include "somm24.h"

namespace group
{

// ================================================================================== //

    double jdtNextSubmission()
    {
        soProbe(206, "%s()\n", __func__);

        require(jdtIn != UNDEF_JOB_INDEX and jdtOut != UNDEF_JOB_INDEX, "Module is not in a valid open state!");
        require(jdtCount != UNDEF_JOB_COUNT, "Module is not in a valid open state!");

        /* TODO POINT: Replace next instruction with your code */
        // throw Exception(ENOSYS, __func__);

        if (jdtCount == 0) {
            return NEVER;
        }

        return jdtTable[jdtOut].submissionTime;
    }

// ================================================================================== //

    Job jdtFetchNext()
    {
        soProbe(207, "%s()\n", __func__);

        require(jdtIn != UNDEF_JOB_INDEX and jdtOut != UNDEF_JOB_INDEX, "Module is not in a valid open state!");
        require(jdtCount != UNDEF_JOB_COUNT, "Module is not in a valid open state!");

        /* TODO POINT: Replace next instruction with your code */
        // throw Exception(ENOSYS, __func__);
        if (jdtCount == 0) {
            throw Exception(EINVAL, "The queue is empty");
        }

        Job jobToReturn = jdtTable[jdtOut];

        jdtOut = (jdtOut + 1) % MAX_JOBS;

        jdtCount--;

        return jobToReturn;
    }

// ================================================================================== //

} // end of namespace group


