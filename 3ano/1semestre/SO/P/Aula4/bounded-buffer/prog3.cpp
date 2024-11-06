#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "utils.h"
#include "thread.h"
#include "fifo.h"

static int sharedValue;
static pthread_mutex_t mutex_access;
static pthread_cond_t cond_var;
static int turn = 0;

void *cthrRoutine(void *arg) {
    int thread_id = *(int *)arg;
    
    while (1) {
        mutex_lock(&mutex_access);
        
        // Wait for this thread's turn
        while (turn != thread_id) {
            cond_wait(&cond_var, &mutex_access);
        }

        // Check if sharedValue has reached 1
        if (sharedValue <= 1) {
            turn = 1 - turn;
            cond_broadcast(&cond_var);
            mutex_unlock(&mutex_access);
            break;
        }

        // Decrement the shared value and print
        sharedValue--;
        printf("Shared Value: %d; Thread ID=%d\n", sharedValue, thread_id);
        
        // Toggle turn to the other thread and signal it
        turn = 1 - turn;
        cond_broadcast(&cond_var);
        mutex_unlock(&mutex_access);
    }

    printf("\n----------------------\nThread %d: Completed\n", thread_id);
    return NULL;
}

int main(void) {
    // Ask for the N1 value and validate
    int N1 = 0;
    while (N1 < 10 || N1 > 20) {
        printf("Insert a value between 10 and 20: ");
        scanf("%d", &N1);
    }
    sharedValue = N1;
    printf("\n----------------------\n");

    // Initialize the mutex and condition variable
    mutex_init(&mutex_access, NULL);
    cond_init(&cond_var, NULL);

    // Create two child threads with alternating decrement roles
    pthread_t cthr[2];
    int ids[2] = {0, 1}; // Thread IDs to control alternation
    thread_create(&cthr[0], NULL, cthrRoutine, &ids[0]);
    thread_create(&cthr[1], NULL, cthrRoutine, &ids[1]);

    // Wait for both child threads to terminate
    thread_join(cthr[0], NULL);
    thread_join(cthr[1], NULL);

    // Cleanup resources
    mutex_destroy(&mutex_access);
    cond_destroy(&cond_var);

    printf("\n----------------------\nMain Thread: Completed\n");
    return 0;
}
