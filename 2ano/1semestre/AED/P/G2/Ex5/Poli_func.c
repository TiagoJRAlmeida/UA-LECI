#include <stdio.h>
#include <ctype.h>

// The coefficients of a degree n polynomial 
// are stored in an array p of size (n + 1) 
// p[0] is the coefficient of the largest degree term 
// p[n] is the coefficient of the zero-degree term 
 
 
// Display a polynomial 
// Pre-Conditions: coef != NULL and degree >= 0 
// Example of produced output:  
// Pol(x) = 1.000000 * x^2 + 4.000000 * x^1 + 1.000000 
void DisplayPol(double* coef, size_t degree) {
    if(coef == NULL || degree < 0){
        printf("Grau ou coeficientes invalidos\n");
        return;
    }

    printf("Pol(x) = ");
    int aux = degree;
    for(int i = 0; i <= degree; i++){
        if(i != degree){
            printf("%.6lf * x^%d + ", coef[i], aux);
            aux--;
        }
        else
            printf("%.6lf\n", coef[i]);
    }
} 
 
 
// Compute the value of a polynomial using Horner’s method: 
// Pre-Conditions: coef != NULL and degree >= 0  
double ComputePol(double* coef, size_t degree, double x) {
    if(coef == NULL || degree < 0){
        printf("Grau ou coeficientes invalidos\n");
        return 0.0;
    }

    double result = coef[0];
    for(int i = 1; i <= degree; i++){
        result = result*x + coef[i];
    }

    return result;
} 
 
// Test example:     
// Pol(x) = 1.000000 * x^2 + 4.000000 * x^1 + 1.000000 
// Pol(2.000000) = 13.000000 
 
 
// Compute the real roots, if any, of a second-degree polynomial 
// Pre-Conditions: coef != NULL and degree == 2 and coef[0] != 0 
// Pre-Conditions: root_1 != NULL and root_2 != NULL 
// Return values: 0 -> no real roots 
//    1 -> 1 real root with multiplicity 2 
//    2 -> 2 distinct real roots 
// The computed root values are returned via the root_1 and root_2 
// pointer arguments 
// Assign 0.0 to the *root_1 and *root_2 if there are no real roots 
//unsigned int  
GetRealRoots(double* coef, size_t degree, double* root_1, double* root_2) {}

int main(void){
    double coef[] = {1.0, 4.0, 1.0};
    size_t degree = (sizeof(coef) / sizeof(coef[0])) - 1;

    DisplayPol(coef, degree);

    printf("\nQuando x = 1: %.2lf", ComputePol(coef, degree, 1)); 
    printf("\nQuando x = 2: %.2lf", ComputePol(coef, degree, 2)); 
    printf("\nQuando x = 5: %.2lf", ComputePol(coef, degree, 5));

    return 0;
}