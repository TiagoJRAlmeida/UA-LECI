/**
 * \defgroup tam TAM -- Common Data Types, Macros and Enumerations
 *
 * \author Artur Pereira - 2024
 */

#ifndef __SOMM24_NM_TAM__
#define __SOMM24_NM_TAM__

#include "dbc.h"
#include "exception.h"
#include "probing.h"

#include <stdint.h>
#include <math.h>

/** @{ */

// ================================================================================== //

#define MAX_JOBS 100                  ///< Maximum number of jobs simulated

#define UNDEF_ADDRESS 0xfffffffe     ///< Pattern meaning the address is undefined

#define UNDEF_SIZE 0xfffffffa           ///< Pattern meaning the size is undefined

#define UNDEF_TIME (-INFINITY)       ///< Pattern meaning the time is undefined
                                     //
#define NEVER (INFINITY)             ///< Pattern meaning an event will never happens in time

#define UNDEF_PID   0xffff          ///< Pattern meaning the PID is undefined

#define UNDEF_COUNT   0xffffffff          ///< Pattern meaning the count is undefined

// ================================================================================== //

/** 
 * \brief Description of a job that will be submitted to the system
 */
struct Job {
    double submissionTime;  ///< The time at which the job will be submitted to the system
    double lifetime;        ///< The amount of time the job takes to execute
    uint32_t memSize;       ///< The size, in number of frames, required by its logical address space
};

// ================================================================================== //

/**
 * \brief Possible states a process can be
 */
enum ProcessState { 
    NEW,        ///< a new process, being prepared to be admitted
    RUNNING,    ///< the process is executing
    // BLOCKED,    ///< the process is blocked
    READY,      ///< the process is ready to execute, waiting for a processor
    SWAPPED,    ///< enough memory is not available yet, so process is waiting for space in swap area
    TERMINATED, ///< the process has already finished its execution
};

// ================================================================================== //

/** \brief Possible memory allocation policies */
enum MemoryAllocationPolicy {
    UndefMemoryAllocationPolicy = -1,   ///< Memory allocation policy undefined 
    BestFit = 1,                        ///< Memory allocation policy set as BestFit
    WorstFit                            ///< Memory allocation policy set as WorstFit
};

// ================================================================================== //

/**
 * \brief Possible processor scheduling policies
 */
enum SchedulingPolicy { 
    UndefSchedulingPolicy = -1,     ///< Scheduling Policy Undefined
    FCFS = 1,                       ///< First Come First Served
    SPN,                            ///< Shortest Job Next
};

// ================================================================================== //

/**
 * \brief Possible swapping in policies
 */
enum SwappingPolicy {
    UndefSwappingPolicy = -1,   ///< Indication that no policy has been yet defined
    FirstProcess = 1,           ///< try to swap in the oldest process in the queue
    FirstFitProcess             ///< try to swap in the oldest process that fits in the biggest available memory block
};

// ================================================================================== //

/**
 * \brief General parameters that drives the simulation
 */
struct SimulationParameters {
    uint32_t jobMaximumMemory;                  ///< maximum memory a job may request
    FILE *jobLoadStream;                        ///< stream where to load future jobs from, being NULL if random generated
    uint32_t jobCount;                          ///< number of jobs, case jobs are to be randomly generated
    uint32_t jobRandomSeed;                     ///< seed to start the random number generator, case jobs are to be randomly generated
    uint32_t memorySize;                        ///< total number of memory units in the system
    uint32_t memoryKernelSize;                  ///< number of memory units used by the kernel
    MemoryAllocationPolicy memoryAllocPolicy;   ///< memory allocation policy to be used in module MEM
    SchedulingPolicy schedulingPolicy;           ///< processor scheduling policy to be used in module RDY
    SwappingPolicy swappingPolicy;              ///< swapping policy to be used in module SWP
};

// ================================================================================== //

/**
 * \brief Macros to select what satellite modules to print
 */
enum PrintSatelliteModules {
    PRINT_NONE = 0x0,   ///< print no satellite modules
    PRINT_JDT = 0x1,    ///< print JDT module
    PRINT_PCT = 0x2,    ///< print PCT module
    PRINT_MEM = 0x4,    ///< print MEM module
    PRINT_RDY = 0x8,    ///< print RDY module
    PRINT_SWP = 0x10,   ///< print SWP module
    PRINT_ALL = 0x1F    ///< print all satellite modules
};

// ================================================================================== //

/** @} */

#endif /* __SOMM24_NM_TAM__ */
