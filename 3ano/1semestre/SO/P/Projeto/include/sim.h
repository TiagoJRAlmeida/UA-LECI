/**
 * \defgroup sim SIM -- Simulation Management
 *
 * \details
 *  This modules provides the functionality that allows to run the simulation, 
 *  both totally or step by step.
 *
 *   The following table presents a list of the functions in this module, including:
 *   - the function name;
 *   - the function ID, that can be used to switch between the binary and group version;
 *   - an estimation of the effort required to implement it;
 *   - a brief description of the function role.
 *   <table>
 *   <tr> <th> \c function <th align="center"> function ID <th align="center"> level <th>role
 *   <tr> <td> \c simInit() <td align="center"> 101 <td> 2 (low) <td> Opens the simulation
 *   <tr> <td> \c simTerm() <td align="center"> 102 <td> 2 (low) <td> Closes the simulation
 *   <tr> <td> \c simPrint() <td align="center"> 103 <td> 4 (medium) <td> Prints the current state of the simulation
 *   <tr> <td> \c simStep() <td align="center"> 104 <td> 6 (high) <td> Run the simulation for one step, if possible
 *   <tr> <td> \c simRun() <td align="center"> 105 <td> 2 (low) <td> Run the simulation for a given number of steps, if possible, or to the end
 *   </table>
 *
 *  \author Artur Pereira - 2024
 */

#ifndef __SOMM24_NM_SIM__
#define __SOMM24_NM_SIM__

#include "tam.h"

#include <stdint.h>

/** @{ */

// ================================================================================== //

/*
 * The set of supporting variables are NOT changeable
 */
extern uint32_t stepCount;          ///< The number of simulation steps run so far
extern double simTime;              ///< The current simulation time
extern double submissionTime;       ///< Time at which the next job will will be submitted to the system
extern double runoutTime;           ///< Time at which the current running process will end its execution
extern uint16_t runningProcess;     ///< PID of the process owning the processor, being 0 if none

// ================================================================================== //

/**
 * \brief Opens the simulation
 * \details
 *   It opens the satellite modules and initializes the internal data structure of the module
 *
 *  This function must proceed as follows:
 *  - call properly the init functions of the other (satellite) modules
 *  - depending on the JDT parameters, either call jdtLoad or jdtRandomFill
 *  - initialize properly the module's internal data structure, defined in file \c frontend/sim.cpp
 *
 * \note Recall that \c jdtLoad and \c jdtRandomFill return the time of submission of the first job
 *
 * \param [in] simulationParameters pointer to the parameters driving the simulation
 */
void simInit(SimulationParameters *simulationParameters);

// ================================================================================== //

/**
 * \brief Closes the simulation
 * \details
 *   The internal data structure of all modules must be put in the closed state
 *
 *  This function must proceed as follows:
 *  - set all internal variables to the close state
 *  - call the close functions of the satellite modules
 */
void simTerm();

// ================================================================================== //

/**
 * \brief Prints the internal state of the simulation
 * \details
 *   The internal state of the SIM module, along with some or all the satellite modules,
 *   must be printed.
 *
 *  This function must proceed as follows:
 *  - based on the second argument, call the print function of satellite modules
 *  - print the state of the SIM module
 *
 * \note 
 *   The printing must produce the same output as the binary version
 *
 * \param [in] fout File stream where to send output 
 * \param [in] satelliteModules Bitwise-or of satellite modules to be printed
 */
void simPrint(FILE *fout, uint32_t satelliteModules);

// ================================================================================== //

/**
 * \brief Process, if possible, a step of the simulation
 * \details
 *  The are 2 possible future events, that come next:
 *  - the submission of a job;
 *  - the runout of the process owning the processor.
 *  
 *  The action to take is to process one of these events, the one that occurs first.
 *  - In case of a submission, a coming job must be admitted for execution,
 *  generating a new process.
 *  Depending on availability of memory to store its address space, 
 *  the new process goes to the ready or swap queue.
 *  - In case of a runout, the running process ends its execution   ,
 *  the memory it uses is released, and swapped processes may have their address space stored
 *  in main memory.
 *  - In any situation, one or more processes, will change state.
 *  - If the processor becomes idle, a ready one, if any, should be put running.
 *
 *  \return \c true if one step was processed; \c false otherwise
 */
bool simStep();

// ================================================================================== //

/**
 * \brief Run the simulation for a given number of steps
 * \details
 *  This function just call the \c simStep an appropriate number of times.
 *
 *  The following must be considered:
 *  - The simulation can reach the end in less than the given number of steps.
 *  - If the given number of steps is zero, the simulation must run til the end.
 *
 * \param [in] cnt Number of simulation steps to execute
 */
void simRun(uint32_t cnt);

// ================================================================================== //

/** @} */

#endif /* __SOMM24_NM_SIM__ */

