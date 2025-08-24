/*
 *  \author Guilherme Matos - 114252
 */

#include "somm24.h"

namespace group
{

// ================================================================================== //

    uint16_t jdtRandomFill(uint32_t seed, uint16_t cnt, uint32_t maxSize)
    {
        soProbe(205, "%s(%u, %u, %#x)\n", __func__, seed, cnt, maxSize);

        require(jdtIn != UNDEF_JOB_INDEX and jdtOut != UNDEF_JOB_INDEX, "Module is not in a valid open state!");
        require(jdtCount != UNDEF_JOB_COUNT, "Module is not in a valid open state!");
        require(cnt == 0 or (cnt >= 2 and cnt <= MAX_JOBS), "Number of jobs is invalid");

        /* TODO POINT: Replace next instruction with your code */
        // throw Exception(ENOSYS, __func__);

        uint16_t jobsRead = 0;
        
        const double minSubmDist = 0.0;
        const double maxSubmDist = 100.0;
        const double stepSubm = 0.1;

        const double minLifetime = 10.0;
        const double maxLifetime = 1000.0;
        const double stepLifetime = 0.1;

        srand(seed);

        // if cnt == 0, cnt = random value in the range [2,MAX_JOBS]
        if (cnt == 0) {
            cnt = (rand() % (MAX_JOBS - 2 + 1) + 2);
        }

        // garantir continuidade
        double submissionTime = (jdtCount > 0) ? jdtTable[(jdtIn - 1 + MAX_JOBS) % MAX_JOBS].submissionTime : 0.0;

        for(uint16_t i = 0; i < cnt; i++) {

            double submissionDist = (rand() / (RAND_MAX + 1.0)) * (maxSubmDist - minSubmDist) + minSubmDist;
            submissionDist = round(submissionDist / stepSubm) * stepSubm;
            submissionTime += submissionDist;  

            // randomly generated in the range [10,1000] in steps of 0.1
            double lifetime = (rand() / (RAND_MAX + 1.0)) * (maxLifetime - minLifetime) + minLifetime;
            lifetime = round(lifetime / stepLifetime) * stepLifetime;

            // greater than zero and not greater the maximum allowed size
            uint32_t memSize = (rand() % maxSize) + 1;
            
            // adicionar jobs à jdtTable
            jdtTable[jdtIn] = {submissionTime, lifetime, memSize};
            jdtIn = (jdtIn + 1) % MAX_JOBS;
            jdtCount++;
            jobsRead++;
        }

        return jobsRead;
    }

// ================================================================================== //

} // end of namespace group

