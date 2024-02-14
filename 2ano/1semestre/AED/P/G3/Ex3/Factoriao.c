#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

int fact(int n) {
    if (n == 2)
        return 2;
    return n * fact(n - 1);
}

int* SepararDigitos(int n, int* tamanho) {
    int i = 0;
    int* digitos = malloc(sizeof(int) * *tamanho);
    if(n == 0){
        *tamanho = 1;
        digitos[i] = 0;
        return digitos;
    }
    while (n > 0) {
        digitos[i] = n % 10;
        n /= 10;
        i++;
    }

    *tamanho = i;
    return digitos;
}

int main(void) {
    int count = 0;

    //Array de fatoriais basicos (0-9)
    int factoriais[10] = {1, 1, 2};
    for (int i = 3; i < 10; i++) {
        factoriais[i] = fact(i);
    }

    for(int num = 0; num < pow(10, 6); num++) {
        int tamanho = 7;
        int* digitos = SepararDigitos(num, &tamanho);
        int sum = 0;
        for (int i = 0; i < tamanho; i++) {
            sum += factoriais[digitos[i]];
        }
        if (num == sum) {
            count++;
            printf("Factoriao: %d\n", num);
        }
        free(digitos);
    }

    return 0;
}
