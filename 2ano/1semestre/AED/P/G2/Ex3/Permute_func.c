#include <stdio.h>

void Permute(int* a, int* b, int* c){
    int aux = *c;
    *c = *b;
    *b = *a;
    *a = aux;
}

int main(void){
    int valor1, valor2, valor3;
    
    printf("Indique primeiro valor: ");
    scanf("%d", &valor1);
    printf("Indique segundo valor: ");
    scanf("%d", &valor2);
    printf("Indique terceiro valor: ");
    scanf("%d", &valor3);

    printf("\n\n\nValor 1: %d", valor1);
    printf("\nValor 2: %d", valor2);
    printf("\nValor 3: %d", valor3);

    Permute(&valor1, &valor2, &valor3);

    printf("\n\n\nValor 1: %d", valor1);
    printf("\nValor 2: %d", valor2);
    printf("\nValor 3: %d", valor3);

    return 0;
}