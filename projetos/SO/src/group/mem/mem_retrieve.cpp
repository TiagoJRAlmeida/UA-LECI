/*
 *  \author Tiago Almeida - 113106
 */

#include "somm24.h"

#include <stdint.h>

namespace group 
{

// ================================================================================== //

    MemNode *memRetrieveNodeFromFreeList(uint32_t size, MemoryAllocationPolicy policy)
    {
        soProbe(409, "%s(%#x, %d)\n", __func__, size, policy);

        require(memAllocationPolicy != UndefMemoryAllocationPolicy, "Module is not in a valid open state!");
        require(memFreeList != UNDEF_MEM_NODE and memOccupiedList != UNDEF_MEM_NODE, "Module is not in a valid open state!");
        require(policy == BestFit or policy == WorstFit, "Allocation policy must be 'BestFit' or 'WorstFit'");

        /* TODO POINT: Replace next instruction with my code */
        // throw Exception(ENOSYS, __func__);

        MemNode* currentNode = memFreeList;
        MemNode* bestOption = NULL;
        
        // Encontrar o melhor node, dependendo da policy
        while (currentNode != NULL) {
            if (currentNode->block.size >= size) {
                if (bestOption == NULL ||
                    (policy == BestFit && currentNode->block.size < bestOption->block.size) ||
                    (policy == WorstFit && currentNode->block.size > bestOption->block.size)) {
                    bestOption = currentNode;
                }
            }
            currentNode = currentNode->next;
        }

        // Se não for encontrado nenhum candidato, devolver uma exceção
        if(bestOption == NULL)
        {
            return UNDEF_MEM_NODE;
        }

        // Retirar o bloco de memória inteiro do memFreeList
        MemNode *previousNode = NULL;
        currentNode = memFreeList;
        while (currentNode != bestOption) {
            previousNode = currentNode;
            currentNode = currentNode->next;
        }
        // Verificar se a melhor opção é no começo da lista ou não e retira-lo
        if (previousNode == NULL) { memFreeList = bestOption->next; } // Se o node encontrado estiver no inicio da lista
        else { previousNode->next = bestOption->next; }
        bestOption->next = NULL;

        // Se o bestOption é maior que o size pedido deve ser dividido.
        if (bestOption->block.size > size) {
            
            // Divisão 1: Bloco de memoria livre
            MemNode *newFreeNode = (MemNode *)malloc(sizeof(MemNode));
            if (newFreeNode == NULL) {
                throw Exception(ENOMEM, __func__);
            }
            newFreeNode->block.size = bestOption->block.size - size;
            newFreeNode->block.start = bestOption->block.start + size;
            newFreeNode->next = NULL;
            memAddNodeToFreeList(newFreeNode);

            // Divisão 2: Bloco de memoria ocupado
            bestOption->block.size = size;
        }

        return bestOption;
    }

// ================================================================================== //

    MemNode *memRetrieveNodeFromOccupiedList(uint32_t address)
    {
        soProbe(410, "%s(%#x)\n", __func__, address);

        require(memAllocationPolicy != UndefMemoryAllocationPolicy, "Module is not in a valid open state!");
        require(memFreeList != UNDEF_MEM_NODE and memOccupiedList != UNDEF_MEM_NODE, "Module is not in a valid open state!");

        /* TODO POINT: Replace next instruction with my code */
        // throw Exception(ENOSYS, __func__);

        MemNode* currentNode = memOccupiedList;
        MemNode* previousNode = NULL;

        // Iterar pelos blocos de memória de memOccupiedList até encontrar o address correto ou até chegar ao fim
        while(currentNode->block.start != address && currentNode != NULL){
            previousNode = currentNode;
            currentNode = currentNode->next;
        }

        // Se não consegui-o encontrar, retorna uma exceção
        if(currentNode == NULL){
            throw Exception(ENOMEM, __func__);
        }

        // Retirar o node encontrado da lista memOccupiedList
        if (previousNode == NULL) { memOccupiedList = currentNode->next; } // Se o node encontrado estiver no inicio da lista
        else { previousNode->next = currentNode->next; }
        currentNode->next = NULL;

        return currentNode;
    }

// ================================================================================== //

} // end of namespace group

