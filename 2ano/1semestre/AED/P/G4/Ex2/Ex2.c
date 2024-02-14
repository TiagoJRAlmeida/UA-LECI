#include <stdio.h>
#include <assert.h>
#include <ctype.h>

int f1(int* parray, size_t n, int* numOper){
    assert(n > 2);
    int r = parray[1] / parray[0];
    for(int i = 1; i < n; i++){
        if(parray[i] != r * parray[i - 1])
            return 0;
        (*numOper)++;
    }
    return 1;
}

int main(void){
    int Array0[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};    
    int Array1[] = {1, 2, 4, 4, 5, 6, 7, 8, 9, 10};   
    int Array2[] = {1, 2, 4, 8, 5, 6, 7, 8, 9, 10};   
    int Array3[] = {1, 2, 4, 8, 16, 6, 7, 8, 9, 10};    
    int Array4[] = {1, 2, 4, 8, 16, 32, 7, 8, 9, 10};   
    int Array5[] = {1, 2, 4, 8, 16, 32, 64, 8, 9, 10};    
    int Array6[] = {1, 2, 4, 8, 16, 32, 64, 128, 9, 10};    
    int Array7[] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 10};  
    int Array8[] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512};

    int* Arrays[] = {Array0, Array1, Array2, Array3, Array4, Array5, Array6, Array7, Array8};
    
    size_t size = sizeof(Arrays[0]) / sizeof(Arrays[0][3]);
    int size1 = sizeof(Array0)/sizeof(Array0[3]);
    printf("-2: %p;  -1:  %p;  0: %d;  1: %d;  2: %d\n\n\n\n",Array0, Arrays[0], Arrays[0][5], size, size1);
    
    for(int i = 0; i < 10; i++){
        int numOper = 0;
        int result = f1(Arrays[i], sizeof(Arrays[i])/sizeof(Arrays[i][0]), &numOper);
        printf("Array %d:\n     Resultado: %d\n     Numero de Operações: %d\n\n", i, result, numOper);
    }
}