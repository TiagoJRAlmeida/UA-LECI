/*
 *  \author Artur Pereira (artur at ua dot pt)
 */

#include "sim.h"
#include "tam.h"
#include "binselection.h"

#include <stdio.h>
#include <stdint.h>

// ================================================================================== //

/*
 * The set of supporting variables are NOT changeable
 */
uint32_t stepCount = UNDEF_COUNT;     // The number of simulation steps already executed
double simTime = UNDEF_TIME;          // The current simulation time
double submissionTime = UNDEF_TIME;   // Time at which the next job will be submitted to the system
double runoutTime = UNDEF_TIME;       // Time at which the current running process will end its execution
uint16_t runningProcess = UNDEF_PID;  // PID of the process owning the processor, being 0 if none

// ================================================================================== //
// ================================================================================== //

namespace binaries {
    void simInit(SimulationParameters *simulationParameters);
    void simTerm();
    void simPrint(FILE *fout, uint32_t satelliteModules);
    bool simStep();
    void simRun(uint32_t cnt);
}

namespace group {
    void simInit(SimulationParameters *simulationParameters);
    void simTerm();
    void simPrint(FILE *fout, uint32_t satelliteModules);
    bool simStep();
    void simRun(uint32_t cnt);
}

// ================================================================================== //

void simInit(SimulationParameters *simulationParameters)
{
    if (soBinSelected(101))
        binaries::simInit(simulationParameters);
    else
        group::simInit(simulationParameters);
}

// ================================================================================== //

void simTerm()
{
    if (soBinSelected(102))
        binaries::simTerm();
    else
        group::simTerm();
}

// ================================================================================== //

void simPrint(FILE *fout, uint32_t satelliteModules)
{
    if (soBinSelected(103))
        binaries::simPrint(fout, satelliteModules);
    else
        group::simPrint(fout, satelliteModules);
}

// ================================================================================== //

bool simStep()
{
    if (soBinSelected(104))
        return binaries::simStep();
    else
        return group::simStep();
}

// ================================================================================== //

void simRun(uint32_t cnt)
{
    if (soBinSelected(105))
        binaries::simRun(cnt);
    else
        group::simRun(cnt);
}

// ================================================================================== //

