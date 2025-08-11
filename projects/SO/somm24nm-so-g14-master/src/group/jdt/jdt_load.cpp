/*
 *  \author Guilherme Matos - 114252
 */

#include "somm24.h"

#include <stdio.h>

#include <string.h>
#include <ctype.h>

namespace group
{

// ================================================================================== //

    uint16_t jdtLoad(FILE *fin, uint32_t maxSize)
    {
        soProbe(204, "%s(%p, %#x)\n", __func__, fin, maxSize);

        require(jdtIn != UNDEF_JOB_INDEX and jdtOut != UNDEF_JOB_INDEX, "Module is not in a valid open state!");
        require(jdtCount != UNDEF_JOB_COUNT, "Module is not in a valid open state!");
        require(fin != nullptr and fileno(fin) != -1, "fin must be a valid file stream");

        /* TODO POINT: Replace next instruction with your code */
        // throw Exception(ENOSYS, __func__);

        char line[256];
        uint16_t jobsRead = 0;
        bool syntacticError = false;
        bool inJobsSection = false;
        double lastSubmissionTime = -1.0;

        while (fgets(line, sizeof(line), fin))
        {
            char *ptr = line;
            // Ignorar espaços no inicio
            while (isspace(*ptr))
                ptr++;

            if (*ptr == '\0' || *ptr == '#')
                continue;

            if (strncmp(ptr, "Begin Jobs", 10) == 0)
            {
                inJobsSection = true;
                continue;
            }
            if (strncmp(ptr, "End Jobs", 8) == 0)
            {
                inJobsSection = false;
                break;
            }

            if (!inJobsSection)
                continue;

            // Remover comentários no final da linha
            char *comment = strchr(ptr, '#');
            if (comment)
                *comment = '\0';

            double submissionTime, lifetime;
            uint32_t memSize;
            if (sscanf(ptr, "%lf ; %lf ; %x", &submissionTime, &lifetime, &memSize) != 3)
            {
                syntacticError = true;
                fprintf(stderr, "Erro de sintaxe na linha: %s\n", line);
                continue;
            }

            if (submissionTime < 0 || submissionTime < lastSubmissionTime || 
                lifetime <= 0 || memSize <= 0 || memSize > maxSize)
            {
                syntacticError = true;
                fprintf(stderr, "Erro semântico na linha: %s\n", line);
                continue;
            }

            lastSubmissionTime = submissionTime;

            // adicionar jobs
            jdtTable[jdtIn] = {submissionTime, lifetime, memSize};
            jdtIn = (jdtIn + 1) % MAX_JOBS;
            jdtCount++;
            jobsRead++;
        }

        if (syntacticError)
        {
            throw Exception(EINVAL, "Erro ao processar o ficheiro");
        }

        return jobsRead;
    }
// ================================================================================== //

} // end of namespace group

