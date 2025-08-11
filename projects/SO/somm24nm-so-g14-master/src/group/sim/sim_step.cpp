/*
 *  \author Tiago Costa (114629); Tiago Almeida - 113106
 */

#include "somm24.h"

namespace group
{

// ================================================================================== //

    bool simStep()
    {
        soProbe(105, "%s()\n", __func__);

        require(simTime != UNDEF_TIME and stepCount != UNDEF_COUNT, "Module not in a valid open state!");
        require(submissionTime != UNDEF_TIME and runoutTime != UNDEF_TIME, "Module is not in a valid open state!");
        require(runningProcess != UNDEF_PID, "Module is not in a valid open state!");

        /* TODO POINT: Replace next instruction with your code */
        // throw Exception(ENOSYS, __func__);

        // Se não houver nada a seguir
        if (submissionTime == NEVER && runoutTime == NEVER) {
            return false;
        }

        // Verificar se primeiro vem o fim do processo atual ou a submissão de um novo
        if (submissionTime <= runoutTime) {
            // Atualizar o simTime
            simTime = submissionTime;

            // Criar o processo para o job seguinte
            Job nextJob = jdtFetchNext();
            

            // Adcionar o novo processo
            uint16_t newRunningProcess = pctNewProcess(simTime, nextJob.lifetime, nextJob.memSize);

            // Verificar se cabe na memória e dependendo disso vai para o SWP ou para o RDY  (swpInsert() ou rdyInsert()) 
            uint32_t biggestFreeBlockSize = memBiggestFreeBlockSize();
            if (biggestFreeBlockSize >= nextJob.memSize){
                uint32_t nextJobMemAddr = memAlloc(nextJob.memSize);
                rdyInsert(newRunningProcess , nextJob.lifetime);
                // Atualizar o processo
                pctUpdateState(newRunningProcess, READY, simTime, nextJobMemAddr);
                // Atualizar coisas extra se for o primeiro momento
                if (stepCount == 0){
                    runningProcess = rdyFetch(); 
                    pctUpdateState(newRunningProcess, RUNNING, simTime, nextJobMemAddr); 
                    runoutTime = submissionTime + nextJob.lifetime;
                }
            } else {
                swpInsert(newRunningProcess , nextJob.memSize);
                pctUpdateState(newRunningProcess, SWAPPED);
            }

            // Atualizar o submissionTime
            submissionTime = jdtNextSubmission();
            
            // Atualizar o stepCount
            stepCount++;

            return true;
        } else {
            // Atualizar o simTime
            simTime = runoutTime;
            uint32_t runningProcessMemStart = pctMemAddress(runningProcess);
            
            // Libertar a memória do processo que vai acabar
            memFree(runningProcessMemStart);
            uint16_t pid = swpFetch(memBiggestFreeBlockSize());

            // Se algum processo couber, tirá-lo do SWP e colocar no RDY
            if (pid != 0){
                double processLifetime = pctLifetime(pid);
                rdyInsert(pid, processLifetime);
                uint32_t processSize = pctMemSize(pid);
                uint32_t processMemStart = memAlloc(processSize);
                // Atualizar o state
                pctUpdateState(pid, READY, simTime, processMemStart);
            }
            
            // Atualizar o state
            pctUpdateState(runningProcess, TERMINATED, simTime);

            // Verificar se há mais processos para correr
            uint16_t newRunningProcessPID = rdyFetch();
            if (newRunningProcessPID != 0) { 
                runningProcess = newRunningProcessPID; 

                // Atualizar o state
                uint32_t newRunningProcessMemStart = pctMemAddress(runningProcess);
                pctUpdateState(runningProcess, RUNNING, simTime, newRunningProcessMemStart);

                // Atualizar o runoutTime
                runoutTime += pctLifetime(runningProcess);

            }
            else {
                runningProcess = 0;
                runoutTime = NEVER;
            }

            // Atualizar o stepCount
            stepCount++;

            return true;
        }
    }

// ================================================================================== //

} // end of namespace group

