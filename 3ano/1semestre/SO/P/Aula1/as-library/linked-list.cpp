#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>

#include "linked-list.h"

/*******************************************************/

SllNode* sllDestroy(SllNode* list){

    SllNode* current = list;
    SllNode* next = current->next;

    while(next != NULL){
        free(current);
        current = next;
        next = next->next;
    }

    return list;
}

/*******************************************************/

void sllPrint(SllNode *list, FILE *fout){
    
}

/*******************************************************/

SllNode* sllInsert(SllNode* list, uint32_t nmec, const char *name){
    assert(name != NULL && name[0] != '\0');
    assert(!sllExists(list, nmec));

    SllNode* current = list;
    SllNode* next = current->next;

    while(next != NULL){
        current = next;
        next = next->next;
    }

    // Criar pessoa

    // Criar um nó

    // inserir a pessoa no nó

    // inserir o nó no next do current

    return list;
}

/*******************************************************/

bool sllExists(SllNode* list, uint32_t nmec){
    SllNode* current = list;
    while(current != NULL){
        Student* current_student = &current->reg;
        if(current_student->nmec == nmec){
            return true;
        }
        current = current->next
    }
    return false;
}

/*******************************************************/

SllNode* sllRemove(SllNode* list, uint32_t nmec){
    assert(list != NULL);
    assert(sllExists(list, nmec));
    
    SllNode* current = list;
    SllNode* previous = list;
    Student* current_student = &current->reg;
    
    while(current_student->nmec != nmec){
        previous = current;
        current = current->next;
        current_student = &current->reg;
    }

    if(previous != current) previous->next = current->next;
    
    free(current);

    return list;
}

/*******************************************************/

const char *sllGetName(SllNode* list, uint32_t nmec){
    assert(list != NULL);
    assert(sllExists(list, nmec));

    SllNode* current = list;
    Student* current_student = &current->reg;

    while(current_student->nmec != nmec){
        current = current->next;
        current_student = &current->reg;
    }

    return current_student->name;
}

/*******************************************************/

SllNode* sllLoad(SllNode *list, FILE *fin, bool *ok){
    assert(fin != NULL);

    if (ok != NULL)
       *ok = false; // load failure

    return NULL;
}

/*******************************************************/

