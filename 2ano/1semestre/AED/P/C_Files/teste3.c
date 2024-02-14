#include <stdio.h>

int maior(int a, int b){
    return a > b; 
}

int main(void){
    //int p1 = 0;
    int p2 = 2;

    printf("True: %d", maior(10, 2));
    printf("\nFalse: %d", maior(2, 10));
    printf("\n%d", p2);
    printf("\n%d", 100%2);
    printf("\nola%dola", 0%100);
    printf("\nola%dola", 99/100);
    printf("\nola%dola", 1%100);
    printf("\nola%dola", 110/100);
}