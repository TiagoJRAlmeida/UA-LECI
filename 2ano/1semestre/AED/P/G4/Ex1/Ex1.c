#include <stdio.h>

int f1(int* parray, size_t n){
    assert(n > 2);
    int nelem = 0;
    for(int i = 1; i < n - 1; i++){
        if(parray[i] == parray[i - 1] + parray[i + 1]){
            nelem++;

        }
    }
    return nelem;
}