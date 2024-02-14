#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int abs(int val) {
    if(val < 0)
        val = -val;
    return val;
} 

float xtoy(float x, int y) {
    int i;
    float result;
    for(i=0, result=1.0; i < abs(y); i++){
        if(y > 0)
            result *= x;
        else
            result /= x;
    }
    return result;
}

int main(void){
    float x;
    int y;

    printf("Introduza um numero: ");
    scanf("%f", &x);
    printf("Introduza o exponente: ");
    scanf("%d", &y);
    float res = xtoy(x, y);
    printf("result: %f^%d = %f", x, y, res);
    return 0;
}