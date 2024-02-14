//
// TO DO : desenvolva um algoritmo para verificar se um numero inteiro positivo
//         e uma capicua
//         Exemplos: 12321 e uma capiacua, mas 123456 nao e
//         USE uma PILHA DE INTEIROS (STACK) e uma FILA DE INTEIROS (QUEUE)
//
// TO DO : design an algorithm to check if the digits of a positive decimal
//         integer number constitue a palindrome
//         Examples: 12321 is a palindrome, but 123456 is not
//         USE a STACK of integers and a QUEUE of integers
//

#include <stdio.h>

#include "IntegersQueue.h"
#include "IntegersStack.h"

int main(void) {
    int num;
    printf("Enter a positive integer: ");
    scanf("%d", &num);

    // Initialize a stack and a queue
    Stack* stack = StackCreate(10);  // Adjust the size as needed
    Queue* queue = QueueCreate(10);  // Adjust the size as needed

    // Push digits onto the stack and enqueue them into the queue
    int originalNum = num;
    while (num > 0) {
        int digit = num % 10; // exemplo: 203 ==> 203 % 10 = 3; 20 % 10 = 0; 2 % 10 = 2
        StackPush(stack, digit);
        QueueEnqueue(queue, digit);
        num /= 10; // exemplo: 202 ==> 202 / 10 = 20; 20 / 10 = 2; 2 / 10 = 0
    }

    // Compare digits from the stack and the queue
    int isPalindrome = 1;  // Assume it's a palindrome
    while (!QueueIsEmpty(queue)) {
        int digitFromStack = StackPop(stack);
        int digitFromQueue = QueueDequeue(queue);
        if (digitFromStack != digitFromQueue) {
            isPalindrome = 0;  // Not a palindrome
            break;
        }
    }

    // Display the result
    if (isPalindrome) {
        printf("%d is a palindrome.\n", originalNum);
    } else {
        printf("%d is not a palindrome.\n", originalNum);
    }

    // Clean up memory
    StackDestroy(&stack);
    QueueDestroy(&queue);

    return 0;
}

