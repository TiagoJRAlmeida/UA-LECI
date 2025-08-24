/*
 *  \author Tiago Almeida - 113106
 */

#include "somm24.h"

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>

namespace group
{

// ================================================================================== //

    void simConfig(FILE *fin, SimParameters *spp)
    {
        soProbe(104, "%s(\"%p\")\n", __func__, fin);

        require(simTime == UNDEF_TIME and stepCount == UNDEF_COUNT, "Module is not in a valid closed state!");
        require(submissionTime == UNDEF_TIME and runoutTime == UNDEF_TIME, "Module is not in a valid closed state!");
        require(runningProcess == UNDEF_PID, "Module is not in a valid closed state!");
        require(fin != nullptr and fileno(fin) != -1, "fin must be a valid file stream");
        require(spp != nullptr, "spp must be a valid pointer");

        /* TODO POINT: Replace next instruction with your code */
        // throw Exception(ENOSYS, __func__);

        char line[256];
        bool inJobsSection = false;
        uint16_t jobsCount = 0;
        spp->jobLoadStream = fin;

        while (fgets(line, sizeof(line), fin))
        {
            char *ptr = line;
            
            while (isspace((unsigned char)*ptr)) 
                ptr++;

            // Se é uma linha vazia ou um comentário, continuar
            if (*ptr == '\0' || *ptr == '#')
                continue;

            // Verificar se é a linha com a tag Begin Jobs
            if (strncmp(ptr, "Begin Jobs", 10) == 0){
                inJobsSection = true;
                continue;
            }

            // Verificar se é a linha com a tag End Jobs
            else if (strncmp(ptr, "End Jobs", 8) == 0){
                inJobsSection = false;
                continue;
            }

            // Se estiver dentro do "Begin Jobs", contar adicionar +1 ao jobsCount
            else if (inJobsSection == true){
                jobsCount++;
                continue;
            }
            
            // Verificar se é a linha com o PIDStart
            else if (strncmp(ptr, "PIDStart", 8) == 0){
                char *valueStart = strchr(ptr, '=');
                if (valueStart != NULL){
                    valueStart++;
                    while (isspace((unsigned char)*valueStart)) { valueStart++; }
                    spp->pidStart = (uint16_t)strtoul(valueStart, NULL, 10); // Decimal
                }
            }

            // Verificar se é a linha com o PIDRandomSeed
            else if (strncmp(ptr, "PIDRandomSeed", 13) == 0){
                char *valueStart = strchr(ptr, '=');
                if (valueStart != NULL){
                    valueStart++;
                    while (isspace((unsigned char)*valueStart)) { valueStart++; }
                    spp->pidRandomSeed = (uint32_t)strtoul(valueStart, NULL, 10); // Decimal
                }
            }

            // Verificar se é a linha com o MemorySize
            else if (strncmp(ptr, "MemorySize", 10) == 0){
                char *valueStart = strchr(ptr, '=');
                if (valueStart != NULL){
                    valueStart++;
                    while (isspace((unsigned char)*valueStart)) { valueStart++; }
                    spp->memorySize = (uint32_t)strtoul(valueStart, NULL, (valueStart[0] == '0' && valueStart[1] == 'x') ? 16 : 10); // Hexadecimal ou decimal
                }
            }

            // Verificar se é a linha com o MemoryKernelSize
            else if (strncmp(ptr, "MemoryKernelSize", 16) == 0){
                char *valueStart = strchr(ptr, '=');
                if (valueStart != NULL){
                    valueStart++;
                    while (isspace((unsigned char)*valueStart)) { valueStart++; }
                    spp->memoryKernelSize = (uint32_t)strtoul(valueStart, NULL, (valueStart[0] == '0' && valueStart[1] == 'x') ? 16 : 10); // Hexadecimal ou decimal
                }
            }

            // Verificar se é a linha com o MemoryAllocationPolicy
            else if (strncmp(ptr, "MemoryAllocationPolicy", 22) == 0){
                char *valueStart = strchr(ptr, '=');
                if (valueStart != NULL){
                    valueStart++;
                    while (isspace((unsigned char)*valueStart)) { valueStart++; }
                    if (strncmp(valueStart, "WorstFit", 8) == 0)
                        spp->memoryAllocPolicy = WorstFit;
                    else if (strncmp(valueStart, "BestFit", 7) == 0)
                        spp->memoryAllocPolicy = BestFit;
                    else
                        throw Exception(ENOSYS, __func__);
                }
            }

            // Verificar se é a linha com o SchedulingPolicy
            else if (strncmp(ptr, "SchedulingPolicy", 16) == 0){
                char *valueStart = strchr(ptr, '=');
                if (valueStart != NULL){
                    valueStart++;
                    while (isspace((unsigned char)*valueStart)) { valueStart++; }
                    if (strncmp(valueStart, "FCFS", 4) == 0)
                        spp->schedulingPolicy = FCFS;
                    else if (strncmp(valueStart, "SPN", 3) == 0)
                        spp->schedulingPolicy = SPN;
                    else
                        throw Exception(ENOSYS, __func__);
                }
            }

            // Verificar se é a linha com o SwappingPolicy
            else if (strncmp(ptr, "SwappingPolicy", 14) == 0){
                char *valueStart = strchr(ptr, '=');
                if (valueStart != NULL){
                    valueStart++;
                    while (isspace((unsigned char)*valueStart)) { valueStart++; }
                    if (strncmp(valueStart, "FIFO", 4) == 0)
                        spp->swappingPolicy = FIFO;
                    else if (strncmp(valueStart, "FirstFit", 8) == 0)
                        spp->swappingPolicy = FirstFit;
                    else
                        throw Exception(ENOSYS, __func__);
                }
            }

            // Verificar se é a linha com o JobMaxSize
            else if (strncmp(ptr, "JobMaxSize", 10) == 0){
                char *valueStart = strchr(ptr, '=');
                if (valueStart != NULL){
                    valueStart++;
                    while (isspace((unsigned char)*valueStart)) { valueStart++; }
                    spp->jobMaxSize = (uint32_t)strtoul(valueStart, NULL, (valueStart[0] == '0' && valueStart[1] == 'x') ? 16 : 10); // Hexadecimal ou decimal
                }
            }

            // Verificar se é a linha com o jobCount - Se o jobCount já tiver sido inicializado, deve ser ignorado
            else if (strncmp(ptr, "JobCount", 8) == 0 && spp->jobCount == 0){
                char *valueStart = strchr(ptr, '=');
                if (valueStart != NULL){
                    valueStart++;
                    while (isspace((unsigned char)*valueStart)) { valueStart++; }
                    spp->jobCount = (uint16_t)strtoul(valueStart, NULL, 10); // Decimal
                }
            }

            // Verificar se é a linha com o JobRandomSeed - Se o JobRandomSeed já tiver sido inicializado, deve ser ignorado
            else if (strncmp(ptr, "JobRandomSeed", 13) == 0 && spp->jobRandomSeed == UNDEF_SEED){
                char *valueStart = strchr(ptr, '=');
                if (valueStart != NULL){
                    valueStart++;
                    while (isspace((unsigned char)*valueStart)) { valueStart++; }
                    uint16_t jobRandomSeed = (uint16_t)strtoul(valueStart, NULL, 10); // Decimal
                    if (jobRandomSeed == 0) { spp->jobRandomSeed = getpid(); }
                    else { spp->jobRandomSeed = jobRandomSeed; }
                }
            }

        }

        // Se tiver o ficheiro tiver a secção de jobs, adicionar
        if (jobsCount != 0){
            spp->jobCount = 0;
            spp->jobRandomSeed = UNDEF_SEED;
        }

        fseek(fin, 0, SEEK_SET);
    }

// ================================================================================== //

} // end of namespace group

