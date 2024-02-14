#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void){
    char string1[100];
    char string2[100];

    printf("Escreva uma String: ");
    scanf("%[^\n]%*c", string1);
    printf("Escreva outra String: ");
    scanf("%[^\n]%*c", string2);

    //Conte os caracteres da primeira string que são letras do alfabeto.
    int cont = 0;
    for(int i = 0; i < strlen(string1); i++){
        if(isalpha(string1[i])){
            cont++;
        }
    }
    printf("\nA primeira string tem %d letras do alfabeto", cont);

    //Conte os caracteres da segunda string que são letras maiúsculas. 
    int cont2 = 0;
    for(int i = 0; i < strlen(string2); i++){
        if(isupper(string2[i])){
            cont2++;
        }
    }
    printf("\nA segunda string tem %d letras maiusculas", cont2);

    //Converta todas as letras maiúsculas, das duas strings, para minúsculas.
    printf("\nLetras minusculas: ");
    //String 1
    for(int i = 0; i < strlen(string1); i++){
        if(isupper(string1[i])){
            string1[i] = tolower(string1[i]); 
        }
    }
    printf("\nPrimeira String: %s", string1);
    //String 2
    for(int i = 0; i < strlen(string2); i++){
        if(isupper(string2[i])){
            string2[i] = tolower(string2[i]); 
        }
    }
    printf("\nSegunda String: %s", string2);

    //Compare  as  duas  strings  resultantes  e  escreva  uma  mensagem  indicando  que  são  iguais,  ou 
    //apresentando as duas strings na sua ordem lexicográfica.
    if(strcmp(string1, string2) == 0){
        printf("\nAs strings são iguais.");
    }
    else{
        printf("\nAs strings sao diferentes.");
    }
    printf("\nOrdem alfabetica: ");
    

    printf("\nPrimeira String: %s", string1);
    printf("\nSegunda String: %s", string2);

    //Crie uma cópia da segunda string.
    
    //Crie e imprima uma string que resulta da concatenação da segunda string com a sua cópia. 

    //!!!!!!!!!Incompleto!!!!!!!!!!!
}