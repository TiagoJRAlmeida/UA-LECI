#include <stdio.h>

#include "utils.h"
#include "thread.h"
#include "fifo.h"

static int sharedValue;

void *cthrRotine(void*)
{
    /* Ask for the N2 value and verify if its correct */
    int N2 = 0;
    while (N2 < 10 or N2 > 20)
    {
        printf("Insert a value between 10 and 20: ");
        scanf("%d", &N2);
    }

    /* Increment the value of the shared variable until its equal to N2 */
    printf("\n-------------------------------\nChild Thread:\n");
    printf("\nSharedValue: %d", sharedValue);
    while (sharedValue != N2)
    {
        sharedValue++;
        printf("\nSharedValue: %d", sharedValue);
    }

    return NULL;
}

int main(void){

    /* Ask for the N1 value and verify if its correct */
    int N1 = 0;
    while (N1 < 1 or N1 > 9)
    {
        printf("Insert a value between 1 and 9: ");
        scanf("%d", &N1);
    }
    sharedValue = N1;

    /* Create the child thread */
    pthread_t cthr;
    thread_create(&cthr, NULL, cthrRotine, NULL);

    /* Wait for the child thread to end */
    thread_join(cthr, NULL);
    
    /* Decrement the value of the shared variable until its equal to 1 */  
    printf("\n\n-------------------------------\nMain Thread:\n");
    printf("\nSharedValue: %d", sharedValue);
    while(sharedValue != 1){
        sharedValue--;
        printf("\nSharedValue: %d", sharedValue);
    }

    return 0;
}