/**
 * \defgroup jdt JDT -- Job Description Table
 *
 * \details
 *  The simulation is driven by an input array (\c jobDescriptionTable), 
 *  representing a sequence of jobs, that will be submitted to the system.
 *
 *  The relevant data for every job is:
 *  - the time of submission
 *  - the time it takes to execute 
 *  - the size of its logical address space
 *  
 *   The supporting data structure is a fixed-size static array.
 *
 *   The following table presents a list of the functions in this module, including:
 *   - the function name;
 *   - the function ID, that can be used to switch between the binary and group version;
 *   - an estimation of the effort required to implement it;
 *   - a brief description of the function role.
 *   <table>
 *   <tr> <th> \c function <th align="center"> function ID <th align="center"> level <th>role
 *   <tr> <td> \c jdtInit() <td align="center"> 201 <td> 2 (low) <td> Initializes the module
 *   <tr> <td> \c jdtTerm() <td align="center"> 202 <td> 2 (low) <td> Closes the module
 *   <tr> <td> \c jdtPrint() <td align="center"> 203 <td> 4 (medium) <td> Prints the current contents of the job description table
 *   <tr> <td> \c jdtLoad() <td align="center"> 204 <td> 6 (high) <td> Fills the job description table from a given file
 *   <tr> <td> \c jdtRandomFill() <td align="center"> 205 <td> 5 (medium high) <td> Randomly fills the job description table
 *   <tr> <td> \c jdtNextSubmission() <td align="center"> 206 <td> 2 (low) <td> Return the time of the next job will be submitted to the system
 *   <tr> <td> \c jdtFetchNext() <td align="center"> 207 <td> 3 (low medium) <td> Remove and return the data of the first job in the queue
 *   </table>
 *
 *  \author Artur Pereira - 2024
 */

#ifndef __SOMM24_NM_JDT__
#define __SOMM24_NM_JDT__

#include "tam.h"

#include <stdint.h>

/** @{ */

// ================================================================================== //

/**
 * \brief List of jobs that will be submitted to the system
 * \details
 *   The list is supported by a circular array.
 *   In its reset state, fields \c in, \c out, and \c count are at zero
 *   and, for every array cell, \c submissionTime is \c UNDEF_TIME, and \c memSize and \c lifetime are zero.
 */
struct JobDescriptionTable {
    uint32_t in;                ///< index of the first empty cell
    uint32_t out;               ///< index of the first occupied cell
    uint32_t count;             ///< actual number of jobs in the job description table
    Job job[MAX_JOBS];          ///< The array supporting the job description table
};

// ================================================================================== //

/**
 * \brief The supporting variable is NOT changeable
 */
extern JobDescriptionTable jobDescriptionTable;     ///< The sequence of jobs to be simulated
extern uint32_t maxAddressSize;          ///< maximum size for the address space of a job

// ================================================================================== //

/**
 * \brief Opens the module, initializing the internal data structure
 * \details
 *  The module's internal data structure, defined in file \c frontend/jdt.cpp, 
 *  must be initialized properly.
 *
 * \param maxSize maximum size the address space of a job may require
 */
void jdtInit(uint32_t maxSize);

// ================================================================================== //

/**
 * \brief Closes the module, setting the internal data structure to the closed state
 * \details
 *   - In the closed state, the supporting data structure has well-defined values.
 *   - This function, should also release any memory it has dynamically allocated.
 */
void jdtTerm();

// ================================================================================== //

/**
 * \brief Prints the internal state of the module
 * \details
 *
 *  - The table elements should be printed in natural order.
 *  - The output must be the same as the one produced by the binary version.
 *  - In case of an error, an appropriate exception must be thrown.
 *  - All exceptions must be of the type defined in this project (Exception).
 *
 * \param [in] fout File stream where printing must be written to
 */
void jdtPrint(FILE *fout);

// ================================================================================== //

/**
 * \brief Fill the job description table from data parsed from a file stream
 * \details
 *   - Syntactically, an input file is a sequence of lines,
 *     each one representing a comment or a job description.
 *   - A line representing a job description is a semi-colon separated sequence of the following
 *     fields:
 *     - a real, positive number, representing the time at which a job will be submitted to the system;
 *     - a real, greater than zero number, representing the duration of its execution;
 *     - an integer, greater then zero number, representing the size of its logical address space
 *   - Lines starting with a hash sign (#) are comments and are to be discarded
 *   - there may be comments in a line representing a job description
 *   - whitespaces (spaces or tabs) are syntactically irrelevant, and may appear any where
 *   - blank lines are also to be discarded
 *
 *  The following must be checked while parsing the input file:
 *  - Submission times should appear in ascending order and can not be negative
 *  - Lifetimes must be greater than zero
 *  - Size of address spaces must be greater than zero and not greater the maximum allowed size
 *  - If case of a **syntactic** or **semantic error**, 
 *    an appropriate error message should be printed to the *standard error*
 *    and the line **discarded**
 *  - In case of a system error, the \c errno error number should be thrown
 *  - All exceptions must be of the type defined in this project (Exception)
 *
 * \param fin file stream where data is to read from
 *
 * \return Time of first submission
 */
uint32_t jdtLoad(FILE *fin);

// ================================================================================== //

/**
 * \brief Randomly fills the job description table
 * \details
 *
 *  The following must be considered:
 *  - If argument \c seed is zero, the seed of the random number generator should be getpid().
 *  - If argument \c n is zero, the number of jobs should be randomly selected between 2
 *    and MAX_JOBS.
 *  - If \c seed is different from zero, the sequence of jobs generated, for a given seed, must always be the same.
 *  - Submission times should be randomly generated in ascending order,
 *    with distances between successive submissions in the range [0,100] in steps of 0.1
 *  - Lifetimes should be randomly generated in the range [10,1000] in steps of 0.1
 *  - Size of address spaces must be greater than zero and not greater the maximum allowed size
 *  - The size of the logical address space should be randomly generated in the range [0x1000, 0x8000]
 *
 * \param [in] n The number of jobs to be generated
 * \param [in] seed The seed for the random number generator
 *
 * \return Time of first submission
 */
uint32_t jdtRandomFill(uint32_t n, uint32_t seed);

// ================================================================================== //

/**
 * \brief Return the submission time of the first job in the job description table
 *
 * \return the time of the first job in the queue or \c NEVER if empty
 */
double jdtNextSubmission();

// ================================================================================== //

/**
 * \brief Remove and return the first job in the job description table
 *
 *  The following must be considered:
 *  - The \c EINVAL exception should be thrown, if the list is empty
 *  - All exceptions must be of the type defined in this project (Exception)
 *  
 * \return the first job in the queue
 */
Job jdtFetchNext();

// ================================================================================== //

/** @} */

#endif /* __SOMM24_NM_JDT__ */

