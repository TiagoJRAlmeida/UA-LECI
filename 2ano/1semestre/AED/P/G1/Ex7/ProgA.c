#include<stdio.h>

void printArray(const char *s, int a[], int size){
    printf("%s:\n", s);
    for(int i=0; i<size; i++){
        printf("%d ", a[i]);
    }
    puts("");
}

void cumSum(int a[], int b[], int size){
    int c = 0;
    for (int i=0; i<size; i++) {
        c += a[i];
        b[i] = c;
    }
}

int main(){

    int a[] = {31,28,31,30,31,30,31,31,30,31,30,31};
    int size = sizeof(a) / sizeof(a[0]);
    printArray("a", a, size);

    int b[12];
    cumSum(a, b, size);
    printArray("b", b, size);
    return 0;
}