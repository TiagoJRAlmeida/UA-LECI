#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>

#include "linked-list.h"

/*******************************************************/

SllNode* sllDestroy(SllNode* list)
{

    SllNode* current = list;
    SllNode* next = current->next;

    while(next != NULL)
    {
        free(current->reg.name);
        free(current);
        current = next;
        next = next->next;
    }

    return list;
}

/*******************************************************/

void sllPrint(SllNode *list, FILE *fout)
{    
    SllNode* current = list;

    while(current != NULL)
    {
        Student* std = &list->reg; 
        fprintf(fout, "%d: %s", std->nmec, std->name);
        current = current->next;
    }
}

/*******************************************************/

SllNode* sllInsert(SllNode* list, uint32_t nmec, const char *name)
{
    assert(name != NULL && name[0] != '\0');
    assert(!sllExists(list, nmec));

    Student* newstd = (Student*)malloc(sizeof(Student));
    if(newstd == NULL) return NULL;

    newstd->name = strdup(name);
    if (newstd->name == NULL) 
    {
        free(newstd);
        return NULL;
    }

    newstd->nmec = nmec;
    
    SllNode* current = list;
    SllNode* next = current->next;

    while(next != NULL)
    {
        current = next;
        next = next->next;
    }

    SllNode* newnode = (SllNode*)malloc(sizeof(SllNode));
    if (newnode == NULL) {
        free(newstd->name);
        free(newstd);
        return NULL;
    }

    newnode->reg = *newstd;
    free(newstd);
    newnode->next = NULL;

    if(list == NULL)
    {
        return newnode;
    }

    current->next = newnode;

    return list;
}

/*******************************************************/

bool sllExists(SllNode* list, uint32_t nmec)
{
    SllNode* current = list;
    while(current != NULL)
    {
        Student* current_student = &current->reg;
        if(current_student->nmec == nmec)
        {
            return true;
        }
        current = current->next;
    }
    return false;
}

/*******************************************************/

SllNode* sllRemove(SllNode* list, uint32_t nmec)
{
    assert(list != NULL);
    assert(sllExists(list, nmec));
    
    SllNode* current = list;
    SllNode* previous = list;
    
    while(current->reg.nmec != nmec)
    {
        previous = current;
        current = current->next;
    }

    if(previous != current) previous->next = current->next;
    
    free(current->reg.name);
    free(current);

    return list;
}

/*******************************************************/

const char *sllGetName(SllNode* list, uint32_t nmec)
{
    assert(list != NULL);
    assert(sllExists(list, nmec));

    SllNode* current = list;
    Student* current_student = &current->reg;

    while(current_student->nmec != nmec)
    {
        current = current->next;
        current_student = &current->reg;
    }

    return current_student->name;
}

/*******************************************************/

SllNode* sllLoad(SllNode *list, FILE *fin, bool *ok)
{
    assert(fin != NULL);

    if (ok != NULL)
       *ok = false; 

    char myString[100];  
    int newnmec;
    char *name;          
    char *delimiter;     

    while (fgets(myString, sizeof(myString), fin)) 
    {
        delimiter = strchr(myString, ';');
        if (delimiter == NULL) {
            continue; 
        }

        *delimiter = '\0';
        newnmec = atoi(myString);

        char *newline = strchr(delimiter + 1, '\n');
        if (newline != NULL) {
            *newline = '\0'; 
        }

        name = strdup(delimiter + 1); 
        if (name == NULL) {
            if (ok != NULL) *ok = false;
            return NULL;
        }

        list = sllInsert(list, newnmec, name);
        if (list == NULL) {
            free(name);
            if (ok != NULL) *ok = false;
            return NULL;
        }

        free(name);
    }

    if (ok != NULL)
        *ok = true;

    return list;
}


/*******************************************************/

