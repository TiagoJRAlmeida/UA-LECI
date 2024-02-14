//Números de Delannoy

#include <stdio.h>
#include <assert.h>

//D(m, n) = 1, se m = 0 ou n = 0 
//D(m, n) = D(m – 1, n) + D(m – 1, n – 1) + D(m, n – 1)


//função recursiva
int D_rec(int m, int n){
    assert(m >= 0);
    assert(n >= 0);
    if(m > 0 && n > 0){
        return D_rec(m - 1, n) + D_rec(m - 1, n - 1) + D_rec(m, n - 1); 
    }
    return 1;
}

//função dinamica
int D_din(int m, int n){
    int d_din[m + 1][n + 1];
    d_din[1][1] = 1;
    for(int i = 0; i <= m; i++){
        for(int j = 0; j <= n; j++){
            if(i == 0 || j == 0)
                d_din[i][j] = 1;
            else
                d_din[i][j] = d_din[i - 1][j] + d_din[i - 1][j - 1] + d_din[i][j - 1];
        }
    }
    return d_din[m][n];
}


int memo[100][100];
//função memoization
int d_memo(int m, int n) {
    if (m == 0 || n == 0)
        return 1;
    if (memo[m][n] != -1)
        return memo[m][n];
    memo[m][n] = d_memo(m - 1, n) + d_memo(m - 1, n - 1) + d_memo(m, n - 1);
    return memo[m][n];
}


//função main
int main(void){
    int m, n;
    printf("Indique um numero (nao negativo):  ");
    scanf("%d", &m);
    printf("Indique outro numero (nao negativo):  ");
    scanf("%d", &n);

    printf("\nNumero de Delannoy (funcao recursiva) de D(%d, %d): %d", m, n, D_rec(m,n));
    printf("\nNumero de Delannoy (funcao dinamica) de D(%d, %d): %d", m, n, D_din(m,n));
    printf("\nNumero de Delannoy (funcao dinamica) de D(%d, %d): %d", m, n, D_memo(m,n));
}