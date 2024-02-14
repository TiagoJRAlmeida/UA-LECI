#include <stdio.h>
#include <ctype.h>
#include <stdlib.h> // Para malloc e free

//4. Desenvolva e teste as três funções seguintes que operam sobre arrays de números reais.  

// Display the contents of array a with n elements 
// Pre-Conditions: a != NULL and n > 0 
// Example of produced output: Array = [ 1.00, 2.00, 3.00 ] 
void DisplayArray(double* a, size_t n) {
    if (a == NULL || n <= 0) {
        printf("Invalid input.\n");
        return;
    }

    printf("Array = [ ");
    for (size_t i = 0; i < n; i++) {
        printf("%.2lf", a[i]); // Exibe cada elemento do array com 2 casas decimais
        if (i < n - 1) {
            printf(", ");
        }
    }
    printf(" ]\n");
} 


// Read the number of elements, allocate the array and read its elements 
// Condition: number of elements > 0 
// Pre-Condition: size_p != NULL 
// Return NULL if memory allocation fails 
// Set *size_p to ZERO if memory allocation fails 
double* ReadArray(size_t* size_p) {
    size_t numElements;

    // Ler o número de elementos do usuário
    printf("Digite o número de elementos: ");
    if (scanf("%zu", &numElements) != 1 || numElements <= 0) {
        printf("Número de elementos inválido.\n");
        *size_p = 0; // Define o tamanho como zero
        return NULL; // Retorna NULL para indicar falha
    }

    // Aloca dinamicamente o array de double
    double* array = (double*)malloc(numElements * sizeof(double));

    // Verificar se a alocação foi bem-sucedida
    if (array == NULL) {
        printf("Falha na alocação de memória.\n");
        *size_p = 0; // Define o tamanho como zero
        return NULL; // Retorna NULL para indicar falha
    }

    // Ler os elementos do array
    printf("Digite os elementos do array:\n");
    for (size_t i = 0; i < numElements; i++) {
        if (scanf("%lf", &array[i]) != 1) {
            printf("Erro ao ler elemento %zu.\n", i);
            free(array); // Libere a memória alocada
            *size_p = 0; // Define o tamanho como zero
            return NULL; // Retorna NULL para indicar falha
        }
    }

    *size_p = numElements; // Define o tamanho correto
    return array; // Retorna o ponteiro para o array alocado
} 
  
 
// Allocate and return a new array with (size_1 + size_2) elements 
// which stores the elements of array_1 followed by the elements of array_2 
// Pre-Conditions: array_1 != NULL and array_2 != NULL 
// Pre-Conditions: size_1 > 0 and size_2 > 0 
// Return NULL if memory allocation fails 
double* Append(double* array_1, size_t size_1, double* array_2, size_t size_2) {} 
 
// Test example:    Array = [ 1.00, 2.00, 3.00 ] 
//                  Array = [ 4.00, 5.00, 6.00, 7.00 ] 
//                  Array = [ 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00 ] 
 
/*ATENÇÃO:  no  final  do  programa  de  teste,  não  se  esqueça  de  libertar  a  memória  alocada 
dinamicamente.*/

int main() {
    double myArray[] = {1.0, 2.0, 3.0};

    size_t length = sizeof(myArray) / sizeof(myArray[0]);

    DisplayArray(myArray, length);


    return 0;
}