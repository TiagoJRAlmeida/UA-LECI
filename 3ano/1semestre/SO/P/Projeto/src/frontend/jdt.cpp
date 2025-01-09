/*
 *  \author Artur Pereira (artur at ua dot pt)
 */

#include "jdt.h"
#include "tam.h"
#include "binselection.h"

#include <stdio.h>
#include <stdint.h>

// ================================================================================== //

/*
 * The set of supporting variables are NOT changeable
 */
JobDescriptionTable jobDescriptionTable;     // The sequence of jobs to be simulated
uint32_t maxAddressSize = UNDEF_SIZE;          // maximum memory size for the address space of a job

// ================================================================================== //
// ================================================================================== //

namespace binaries {
    void jdtInit(uint32_t maxSize);
    void jdtTerm();
    void jdtPrint(FILE *fout);
    uint32_t jdtLoad(FILE *fin);
    uint32_t jdtRandomFill(uint32_t n, uint32_t seed);
    double jdtNextSubmission();
    Job jdtFetchNext();
}

namespace group {
    void jdtInit(uint32_t maxSize);
    void jdtTerm();
    void jdtPrint(FILE *fout);
    uint32_t jdtLoad(FILE *fin);
    uint32_t jdtRandomFill(uint32_t n, uint32_t seed);
    double jdtNextSubmission();
    Job jdtFetchNext();
}

// ================================================================================== //

void jdtInit(uint32_t maxSize)
{
    if (soBinSelected(201))
        binaries::jdtInit(maxSize);
    else
        group::jdtInit(maxSize);
}

// ================================================================================== //

void jdtTerm()
{
    if (soBinSelected(202))
        binaries::jdtTerm();
    else
        group::jdtTerm();
}

// ================================================================================== //

void jdtPrint(FILE *fout)
{
    if (soBinSelected(203))
        binaries::jdtPrint(fout);
    else
        group::jdtPrint(fout);
}

// ================================================================================== //

uint32_t jdtLoad(FILE *fin)
{
    if (soBinSelected(204))
        return binaries::jdtLoad(fin);
    else
        return group::jdtLoad(fin);
}

// ================================================================================== //

uint32_t jdtRandomFill(uint32_t n, uint32_t seed)
{
    if (soBinSelected(205))
        return binaries::jdtRandomFill(n, seed);
    else
        return group::jdtRandomFill(n, seed);
}

// ================================================================================== //

double jdtNextSubmission()
{
    if (soBinSelected(206))
        return binaries::jdtNextSubmission();
    else
        return group::jdtNextSubmission();
}

// ================================================================================== //

Job jdtFetchNext()
{
    if (soBinSelected(207))
        return binaries::jdtFetchNext();
    else
        return group::jdtFetchNext();
}

// ================================================================================== //

