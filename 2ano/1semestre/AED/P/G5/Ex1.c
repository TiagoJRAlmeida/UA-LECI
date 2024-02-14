#include <stdio.h>
#include <assert.h>
//Funções recursivas

int calls = 0;

//função 1:
int f1(int n){
    assert(n > 0);
    if(n > 1){
        calls++;
        return f1(n/2) + n;
    }
    return 1;
}


//função main:
int main(void) {
  int n, r;

  printf("Valor de n (inteiro nao-negativo): ");
  scanf("%d", &n);

  printf("\nCalculo do valor da recorrencia 1:\n\n");
  for (int i = 1; i <= n; i++) {
    calls = 0;
    r = f1(i);
    printf("T\(%3d) = %6d", i, r);
    printf(" --- Numero de chamadas recursivas = %3d\n", calls);
  }
  printf("\n\n");
  return 0;
}