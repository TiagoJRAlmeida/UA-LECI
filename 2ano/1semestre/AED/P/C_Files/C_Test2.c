#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int* SepararDigitos(int n, int *tamanho) {
    int i = 0;
    int *digitos = malloc(sizeof(int) * *tamanho);
    while(n > 0){
        digitos[i] = n % 10;
        n /= 10;
        i++;
    }
    
    *tamanho = i;    
    return digitos;
}

int ContarDigitos(int n){
    for(int i = 10; i < pow(10, 6); i*=10){
        if(n % i == 0){
            return i;
        }
    }
    return 0;
}

int main(void){
    int numero = 123456789;
    int tamanho = ContarDigitos(numero);
    int *digitos = SepararDigitos(numero, &tamanho);
    printf("-----teste----\n");
    printf("Tamanho: %d\n", tamanho);
    for(int i = 0; i < tamanho; i++){
        printf("\nElemento %d: %d", i, digitos[i]);
    }
    printf("\n-----teste----");
    
    free(digitos);
    return 0;
}