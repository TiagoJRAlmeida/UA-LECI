#include <stdio.h>

void SelectionSort(int* a, unsigned int n){
    for(int i = 0; i < n - 1; i++){
        int indiceMenor = i;
        for(int j = i + 1; j < n; j++){
            if(a[j] < a[indiceMenor])
                indiceMenor = j;
        }
        if(indiceMenor != i){
            int temp = a[i];
            a[i] = a[indiceMenor];
            a[indiceMenor] = temp;
        }
    }
}

int main(void){
    int array[5] = {5, 3, 2, 4 , 1};
    SelectionSort(array, 5);
    for(int i = 0; i < 5; i++){
        printf("%d", array[i]);
    } 
    printf("\n");
}