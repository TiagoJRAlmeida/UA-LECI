#include <assert.h>
#include <stdio.h>

int calls = 0;

//função 3
int f3(int n){
    assert(n > 0);
    if(n == 1)
        return 1;
    else if(n % 2 == 0){
        calls++;
        return 2 * f3(n/2) + n;
    }
    else{
        calls += 2;
        return f3(n/2) + f3((n+1)/2) + n;
    }
}

//função main:
int main(void) {
  int n, r;

  printf("Valor de n (inteiro nao-negativo): ");
  scanf("%d", &n);

  printf("\nCalculo do valor da recorrencia 1:\n\n");
  for (int i = 1; i <= n; i++) {
    calls = 0;
    r = f3(i);
    printf("T\(%3d) = %6d", i, r);
    printf(" --- Numero de chamadas recursivas = %3d\n", calls);
  }
  printf("\n\n");
  return 0;
}