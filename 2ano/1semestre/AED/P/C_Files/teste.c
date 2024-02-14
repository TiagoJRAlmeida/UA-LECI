#include <stdio.h>

int main(void){

    char s[] = "Hello";
    char *p = s;
    while(*p != '\0'){
        printf("%p = ", p);
        printf("%c\n", *p++);
    }
}