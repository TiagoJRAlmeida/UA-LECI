/**
 * @file
 *
 * \brief A hospital pediatric urgency with a Manchester triage system.
 */

#include  <stdio.h>
#include  <stdlib.h>
#include  <string.h>
#include  <libgen.h>
#include  <unistd.h>
#include  <sys/wait.h>
#include  <sys/types.h>
#include  <thread.h>
#include  <math.h>
#include  <stdint.h>
#include  <signal.h>
#include  <utils.h>
#include  "settings.h"
#include  "pfifo.h"

/* DO NOT CHANGE THE FOLLOWING VALUES, run program with option -h to set a different values */

static int npatients = 4;  ///< number of patients
static int nnurses = 1;    ///< number of triage nurses
static int ndoctors = 1;   ///< number of doctors

#define USAGE "Synopsis: %s [options]\n" \
   "\t----------+-------------------------------------------------------------\n" \
   "\t  Option  |          Description                                        \n" \
   "\t----------+-------------------------------------------------------------\n" \
   "\t -p num   | number of patients (dfl: %d, min: %d, max: %d)              \n" \
   "\t -n num   | number of nurses (dfl: %d, min: %d, max: %d)                \n" \
   "\t -d num   | number of doctors (dfl: %d, min: %d, max: %d)               \n" \
   "\t -h       | this help                                                   \n" \
   "\t----------+-------------------------------------------------------------\n", \
   basename(argv[0]), npatients, 1, MAX_PATIENTS, nnurses, 1, MAX_NURSES, ndoctors, 1, MAX_DOCTORS


// TODO point: changes may be required in these date structures

/**
 * \brief Patient data structure
 */
typedef struct
{
   char name[MAX_NAME+1];
   int done; // 0: waiting for consultation; 1: consultation finished
   // TODO point: if necessary, add new fields here
   pthread_mutex_t patient_mutex;
   pthread_cond_t is_done;
} Patient;

typedef struct
{
   int num_patients;
   Patient all_patients[MAX_PATIENTS];
   PriorityFIFO triage_queue;
   PriorityFIFO doctor_queue;
   // TODO point: if necessary, add new fields here
} HospitalData;

HospitalData * hd = NULL;

// TODO point: if necessary, add module variables here


/**
 *  \brief verification tests:
 */
#define check_valid_patient(id) do { check_valid_patient_id(id); check_valid_name(hd->all_patients[id].name); } while(0)
#define check_valid_nurse(id) do { check_valid_nurse_id(id); } while(0)
#define check_valid_doctor(id) do { check_valid_doctor_id(id); } while(0)

int random_manchester_triage_priority();
void new_patient(Patient* patient); // initializes a new patient
void random_wait();


/* ************************************************* */

// TODO point: changes may be required to this function
void init_simulation(int np)
{
   printf("Initializing simulation\n");
   hd = (HospitalData*)mem_alloc(sizeof(HospitalData)); // mem_alloc is a malloc with NULL pointer verification
   memset(hd, 0, sizeof(HospitalData));
   hd->num_patients = np;
   init_pfifo(&hd->triage_queue);
   init_pfifo(&hd->doctor_queue);
   for(int i = 0; i < np; i++){
      mutex_init(&(hd->all_patients[i].patient_mutex), NULL);
      cond_init(&(hd->all_patients[i].is_done), NULL); 
   }
}


/* ************************************************* */

// TODO point: changes may be required to this function
void term_simulation(int np) {
   // DO NOT WAIT THE TERMINATION OF ACTIVE ENTITIES IN THIS FUNCTION!
   // This function is just to release the allocated resources

   printf("Releasing resources\n");
   term_pfifo(&hd->doctor_queue);
   term_pfifo(&hd->triage_queue);
   for(int i = 0; i < np; i++){
      mutex_destroy(&(hd->all_patients[i].patient_mutex));
      cond_destroy(&(hd->all_patients[i].is_done)); 
   }
   free(hd);
   hd = NULL;
}

/* ************************************************* */

// TODO point: changes may be required to this function
int nurse_iteration(int id) // return value can be used to request termination
{
   check_valid_nurse(id);
   printf("\e[34;01mNurse %d: get next patient\e[0m\n", id);
   int patient = retrieve_pfifo(&hd->triage_queue);
   // TODO point: PUT YOUR NURSE TERMINATION CODE HERE:
   if (patient == -1) 
   {
      return 1;
   }
   check_valid_patient(patient);
   printf("\e[34;01mNurse %d: evaluate patient %d priority\e[0m\n", id, patient);
   int priority = random_manchester_triage_priority();
   printf("\e[34;01mNurse %d: add patient %d with priority %d to doctor queue\e[0m\n", id, patient, priority);
   insert_pfifo(&hd->doctor_queue, patient, priority);

   return 0;
}

/* ************************************************* */

// TODO point: changes may be required to this function
int doctor_iteration(int id) // return value can be used to request termination
{
   check_valid_doctor(id);
   printf("\e[32;01mDoctor %d: get next patient\e[0m\n", id);
   int patient = retrieve_pfifo(&hd->doctor_queue);
   // TODO point: PUT YOUR DOCTOR TERMINATION CODE HERE:
   if (patient == -1) 
   {
      return 1;
   }
   check_valid_patient(patient);
   printf("\e[32;01mDoctor %d: treat patient %d\e[0m\n", id, patient);
   random_wait();
   printf("\e[32;01mDoctor %d: patient %d treated\e[0m\n", id, patient);
   // TODO point: PUT YOUR PATIENT CONSULTATION FINISHED NOTIFICATION CODE HERE:
   mutex_lock(&(hd->all_patients[patient].patient_mutex));
   hd->all_patients[patient].done = 1;
   cond_broadcast(&(hd->all_patients[patient].is_done));
   mutex_unlock(&(hd->all_patients[patient].patient_mutex));
   return 0;
}

/* ************************************************* */

void patient_goto_urgency(int id)
{
   new_patient(&hd->all_patients[id]);
   check_valid_name(hd->all_patients[id].name);
   printf("\e[30;01mPatient %s (number %d): get to hospital\e[0m\n", hd->all_patients[id].name, id);
   insert_pfifo(&hd->triage_queue, id, 1); // all elements in triage queue with the same priority!
}

// TODO point: changes may be required to this function
void patient_wait_end_of_consultation(int id)
{
   check_valid_name(hd->all_patients[id].name);
   // TODO point: PUT YOUR WAIT CODE FOR FINISHED CONSULTATION HERE:
   // while(!hd->all_patients[id].done); // ERRADO: Tenho de usar mutex e cond
   mutex_lock(&(hd->all_patients[id].patient_mutex));
   while(!hd->all_patients[id].done)
   {
      cond_wait(&(hd->all_patients[id].is_done), &(hd->all_patients[id].patient_mutex));
   }
   mutex_unlock(&(hd->all_patients[id].patient_mutex));
   printf("\e[30;01mPatient %s (number %d): health problems treated\e[0m\n", hd->all_patients[id].name, id);
}

// TODO point: changes are required to this function
void patient_life(int id)
{
   patient_goto_urgency(id);
   patient_wait_end_of_consultation(id);
   memset(&(hd->all_patients[id]), 0, sizeof(Patient)); // patient finished
}

/* ************************************************* */

// TODO point: if necessary, add extra functions here:
void* patient_thread(void* args)
{
   int patient_id = *(int*)args;
   patient_life(patient_id);
   return NULL;
}

void* nurse_thread(void* args)
{
   int nurse_id = *(int*)args;
   while(!nurse_iteration(nurse_id))
      ;
   return NULL;
}

void* doctor_thread(void* args)
{
   int doctor_id = *(int*)args;
   while(!doctor_iteration(doctor_id))
      ;
   return NULL;
}

/* ************************************************* */

int main(int argc, char *argv[])
{
   /* command line processing */
   int option;
   while ((option = getopt(argc, argv, "p:n:d:h")) != -1)
   {
      switch (option)
      {
         case 'p':
            npatients = atoi(optarg);
            if (npatients < 1 || npatients > MAX_PATIENTS)
            {
               fprintf(stderr, "Invalid number of patients!\n");
               return EXIT_FAILURE;
            }
            break;
         case 'n':
            nnurses = atoi(optarg);
            if (nnurses < 1 || nnurses > MAX_NURSES)
            {
               fprintf(stderr, "Invalid number of nurses!\n");
               return EXIT_FAILURE;
            }
            break;
         case 'd':
            ndoctors = atoi(optarg);
            if (ndoctors < 1 || nnurses > MAX_DOCTORS)
            {
               fprintf(stderr, "Invalid number of doctors!\n");
               return EXIT_FAILURE;
            }
            break;
         case 'h':
            printf(USAGE);
            return EXIT_SUCCESS;
         default:
            fprintf(stderr, "Non valid option!\n");
            fprintf(stderr, USAGE);
            return EXIT_FAILURE;
      }
   }

   /* start random generator */
   srand(getpid());

   /* init simulation */
   init_simulation(npatients);

   // TODO point: REPLACE THE FOLLOWING DUMMY CODE WITH code to launch
   // active entities and code to properly terminate the simulation.
   pthread_t pthr[npatients];
   pthread_t nthr[nnurses];
   pthread_t dthr[ndoctors];
   int patient_id[npatients];
   int nurse_id[nnurses];
   int doctor_id[ndoctors];

   for(int i = 0; i < npatients; i++)
   {
      patient_id[i] = i + 1;
      thread_create(&pthr[i], NULL, patient_thread, &patient_id[i]);
   }

   for(int i = 0; i < nnurses; i++)
   {
      nurse_id[i] = i + 1;
      thread_create(&nthr[i], NULL, nurse_thread, &nurse_id[i]);
   }

   for(int i = 0; i < ndoctors; i++)
   {
      doctor_id[i] = i + 1;
      thread_create(&dthr[i], NULL, doctor_thread, &doctor_id[i]);
   }


   for(int i = 0; i < npatients; i++)
   {
      thread_join(pthr[i], NULL);
   }

   /* close fifos */
   close_pfifo(&hd->triage_queue);
   close_pfifo(&hd->doctor_queue);

   for(int i = 0; i < nnurses; i++)
   {
      thread_join(nthr[i], NULL);
   }

   for(int i = 0; i < ndoctors; i++)
   {
      thread_join(dthr[i], NULL);
   }


   /* terminate simulation */
   term_simulation(npatients);

   return EXIT_SUCCESS;
}


/* IGNORE THE FOLLOWING CODE */

int random_manchester_triage_priority()
{
   int result;
   int perc = random_int(0, 100);
   if (perc < 10)
      result = RED;
   else if (perc < 30)
      result = ORANGE;
   else if (perc < 50)
      result = YELLOW;
   else if (perc < 75)
      result = GREEN;
   else
      result = BLUE;
   return result;
}

static char **names = (char *[]) {
   "Ana", "Miguel", "Luis", "Joao",
   "Artur", "Maria", "Luisa", "Mario",
   "Augusto", "Antonio", "Jose", "Alice",
   "Almerindo", "Gustavo", "Paulo", "Paula",
   NULL};
static int names_len = 16;

char* random_name()
{
   return names[random_int(0, names_len-1)];
}

void new_patient(Patient* patient)
{
   strcpy(patient->name, random_name());
   patient->done = 0;
}

void random_wait()
{
   usleep((useconds_t)random_int(0, MAX_WAIT));
}
