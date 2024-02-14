#include <stdio.h>

int main(void){
    char s[] = "Hello";
    char *p = s;
    int i;
    
    for(i = 0; i < 5; i++){
        printf("%p = ", p);
        printf("%c = ", *p);
        printf("%c\n", (*p)++);  //p nunca é incrementado
    }
}