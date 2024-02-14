#include <stdio.h>

int main(void){
    
    int array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int *pointer;

    printf("%p\n", array);

    pointer = array;

    printf("%p\n", pointer);

    printf("Array[0]: %d\n", *pointer);
    printf("Array[0]: %d\n", *array);

    printf("Array[1]: %d\n", *(pointer + 5));
    printf("Array[1]: %d\n", *(array + 5));

    return 0;
}