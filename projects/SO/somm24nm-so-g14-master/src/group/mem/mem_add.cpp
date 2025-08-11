/*
 *  \author Tiago Almeida - 113106 Rafael Dias N114258
 */

#include "somm24.h"

#include <stdint.h>

namespace group 
{

// ================================================================================== //

    void memAddNodeToFreeList(MemNode *p)
    {
        soProbe(407, "%s(%p)\n", __func__, p);

        require(memAllocationPolicy != UndefMemoryAllocationPolicy, "Module is not in a valid open state!");
        require(memFreeList != UNDEF_MEM_NODE and memOccupiedList != UNDEF_MEM_NODE, "Module is not in a valid open state!");
        require(p != nullptr, "p must be a valid pointer");

        /* TODO POINT: Replace next instruction with my code */
        // throw Exception(ENOSYS, __func__);

    p->next = NULL;

    // Caso 1: Lista vazia, insere como único bloco
    if (memFreeList == NULL) {
        memFreeList = p;
        return;
    }

    MemNode *current = memFreeList;
    MemNode *previous = NULL;

    // Caso 2.1: Fusão antes do primeiro bloco
    if (p->block.start + p->block.size == current->block.start) {
        current->block.start = p->block.start;
        current->block.size += p->block.size;
        free(p);
        return;
    }

    // Caso 2.2: Inserção antes do primeiro bloco
    if (p->block.start < current->block.start) {
        p->next = current;
        memFreeList = p;
        return;
    }

    // Percorre a lista para encontrar posição de inserção ou fusão
    while (current != NULL) {
        // Caso 3: Fusão entre anterior e atual
        if (previous != NULL && previous->block.start + previous->block.size == p->block.start &&
            p->block.start + p->block.size == current->block.start) {
            previous->block.size += p->block.size + current->block.size;
            previous->next = current->next;
            free(current);
            free(p);
            return;
        }

        // Caso 4: Fusão com o bloco atual
        if (p->block.start + p->block.size == current->block.start) {
            current->block.start = p->block.start;
            current->block.size += p->block.size;
            free(p);
            return;
        }

        // Caso 5: Fusão com o bloco anterior
        if (previous != NULL && previous->block.start + previous->block.size == p->block.start) {
            previous->block.size += p->block.size;
            free(p);
            return;
        }

        // Caso 6: Inserção entre dois blocos
        if (previous != NULL && previous->block.start + previous->block.size < p->block.start &&
            (current == NULL || p->block.start + p->block.size < current->block.start)) {
            previous->next = p;
            p->next = current;
            return;
        }

        previous = current;
        current = current->next;
    }

    // Caso 7: Inserção ao final da lista
    if (previous != NULL) {
        previous->next = p;
    }
}

// ================================================================================== //

    void memAddNodeToOccupiedList(MemNode *p)
    {
        soProbe(408, "%s(%p)\n", __func__, p);

        require(memAllocationPolicy != UndefMemoryAllocationPolicy, "Module is not in a valid open state!");
        require(memFreeList != UNDEF_MEM_NODE and memOccupiedList != UNDEF_MEM_NODE, "Module is not in a valid open state!");
        require(p != nullptr, "p must be a valid pointer");

        /* TODO POINT: Replace next instruction with my code */
        // throw Exception(ENOSYS, __func__);

        p->next = NULL;

        // Caso 1: Lista de blocos ocupados está vazia
        if (memOccupiedList == NULL) {
            memOccupiedList = p;
            return;
        }

        MemNode *current = memOccupiedList;
        MemNode *previous = NULL;

        // Para a lista estar ordenada
        while (current != NULL && current->block.start < p->block.start) {
            previous = current;
            current = current->next;
        }


        if (previous == NULL) {
            // Inserir no início da lista
            p->next = memOccupiedList;
            memOccupiedList = p;
        } 
        else {
            p->next = current;
            previous->next = p;
        }
    }

// ================================================================================== //

} // end of namespace group

