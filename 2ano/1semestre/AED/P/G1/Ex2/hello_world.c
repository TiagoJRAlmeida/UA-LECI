#include<stdio.h>

int main(void){
    puts("(puts) Hello World!");
    
    FILE *file = fopen("teste.txt", "w");
    if (file != NULL){
        fputs("(fputs) Hello World!", file);
        fclose(file);
    } else {
        perror("Erro ao abrir o arquivo");
    }
    
    printf("%s", "(printf) Hello World!\n");
    return 0;
}