
// JMR, 2021

// Complete the functions (marked by ...)
// so that it passes all tests in PersonTest.

#include "Person.h"

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// This variable stores the last ID that was assigned to a Person.
// It should be used to assign serial, unique IDs automatically upon creation.
// The first person will have id=1, the second id=2, etc.
static int lastID = 0;

// Alocate and store a Person.
// Returns the pointer to the new structure,
// or NULL if allocation fails.
// The names are copied to internally allocated memory.
Person *PersonCreate(const char *fname, const char *lname, int yy, int mm,
                     int dd) {
  Person* p = (Person*)malloc(sizeof(Person));
  if(p == NULL) return NULL;
  lastID++; 
  p->firstName = strdup(fname);
  p->lastName = strdup(lname);
  p->birthDate = *DateCreate(yy, mm, dd);
  p->id = lastID;
  return p;
}

// Free the memory pointed to by *pp and by the names inside it,
// and invalidate *pp contents.
// Precondition: *pp must not be NULL.
// Postcondition: *pp is set to NULL.
void PersonDestroy(Person **pp) {
  assert(*pp != NULL);
  Person* p = *pp;
  free(p);
  *pp = NULL;
}

// Prints a person formatted as "[id, lastname, firstname, birthdate]",
// followed by a suffix string.
void PersonPrintf(Person *p, const char *suffix) {
  if (p == NULL)
    printf("NULL%s", suffix);
  else
    printf("(%d, %s, %s, %s)%s", p->id, p->lastName, p->firstName,
           DateFormat(&(p->birthDate), YMD), suffix);
}

// Compare birth dates of two persons.
// Return a negative/positive integer if p1 was born before/after p2.
// Return zero if p1 and p2 were born on the same date.
int PersonCompareByBirth(const Person *p1, const Person *p2) {
  return DateCompare((const Date *)&p1->birthDate,(const Date *)&p2->birthDate);
}

// Compare two persons by last name, then first name (if last name is the same).
// Return a -/+/0 integer if p1 precedes/succeeds/is equal to p2.
int PersonCompareByLastFirstName(const Person *p1, const Person *p2) {
  int min = strlen(p1->lastName) < strlen(p2->lastName) ? strlen(p1->lastName) : strlen(p2->lastName); 
  for(int i = 0; i < min; i++){
    if(p1->lastName[i] < p2->lastName[i]) return -1;
    else if(p1->lastName[i] > p2->lastName[i]) return 1;
  }

  if(strlen(p1->lastName) < strlen(p2->lastName)) return 1;
  else if(strlen(p1->lastName) > strlen(p2->lastName)) return -1;

  int min1 = strlen(p1->firstName) < strlen(p2->firstName) ? strlen(p1->firstName) : strlen(p2->firstName); 
  for(int i = 0; i < min1; i++){
    if(p1->firstName[i] < p2->firstName[i]) return -1;
    else if(p1->firstName[i] > p2->firstName[i]) return 1;
  }

  if(strlen(p1->firstName) < strlen(p2->firstName)) return 1;
  else if(strlen(p1->firstName) > strlen(p2->firstName)) return -1;

  return 0;
}
