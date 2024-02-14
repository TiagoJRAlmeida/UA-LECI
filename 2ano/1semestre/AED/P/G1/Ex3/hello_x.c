#include<stdio.h>

int main(void){
    
    char nome[50];
    puts("Uso do gets()");
    printf("Indique o seu nome: ");
    gets(nome);
    printf("Hello %s!\n", nome);

    char nome1[5];
    puts("\nUso do fgets()");
    printf("Indique o seu nome: ");
    fgets(nome1, sizeof(nome1), stdin); // Lê uma linha da entrada padrão
    printf("Hello %s!\n", nome1);

    char nome2[50];
    puts("\nUso do gets()");
    printf("Indique o seu nome: ");
    scanf("%s", nome2); //Lê uma palavra (até encontrar espaço ou quebra de linha) ps: Se houver resto não lido anteriormente, vai ler agora.
    printf("Hello %s!\n", nome2);
    return 0;
}