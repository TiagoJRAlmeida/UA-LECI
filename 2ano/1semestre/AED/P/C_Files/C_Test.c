#include<stdio.h>
#include <stdbool.h>

bool isPalindrome(int x) {
    
    if(x < 0) return false;

    // Count digits
    int count = 1;
    int aux = x;
    while(aux > 10){
        aux /= 10;
        count++;
    }
    char str[count];
    sprintf(str, "%d", x);
    for(int i = 0; i < count; i++){
        if(str[i] != str[count - 1 - i]){
            return false;
        }
    }

    return true;
}

enum values{
    I = 1,
    V = 5,
    X = 10,
    L = 50,
    C = 100,
    D = 500,
    M = 1000
};

int romanToInt(char* s) {
    int sum = 0;
    
    for(int i = 0; i < s.length() - 1; i++){
        switch(s[i]){
            case "I": sum += I; break;
            case 'V': sum += V; break;
            case 'X': sum += X; break;
            case 'L': sum += L; break;
            case 'C': sum += C; break;
            case 'D': sum += D; break;
            case 'M': sum += M; break;
        }
    }    

    return sum;
}

int main(void){
    printf("Hello world!\n");
    char* str = "III";
    printf("%d\n", romanToInt(str));
    return 0;
}