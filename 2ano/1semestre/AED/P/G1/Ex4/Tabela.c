#include<stdio.h>
#include<math.h>

int main(void){
    int linhas;
    int i = 0;
    printf("Linhas da tabela: ");
    scanf("%d", &linhas);
    printf("%3s %4s %10s\n", "N", "N^2", "sqrt(N)");
    puts("-------------------");
    while(i < linhas){
        printf("%3d %4d %10.5lf\n", i, i*i, sqrt(i));
        i++;
    }
    return 0;
}