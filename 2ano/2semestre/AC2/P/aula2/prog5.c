#include <detpic32.h>

// Continuação do prog4.c, mas agora a tecla 'N' irá parar o contador, 
// e a tecla 'R' irá retomar o contador. 


void delay(unsigned int ms){
    resetCoreTimer();
    while(readCoreTimer() < 20000 * ms);
}

int main(void){
    int cnt1 = 0;
    int cnt5 = 0;
    int cnt10 = 0;
    int key;

    while(1){
        key = inkey();
        if(key == 78 || key == 110){
            while(key != 82 && key != 114){
                key = inkey();
            }
        }
        else{
            delay(100);
            cnt10++;
            if(cnt10 >= 10 && cnt10 % 10 == 0){ cnt1++; }
            if(cnt10 >= 2 && cnt10 % 2 == 0) { cnt5++; }
            
            printInt(cnt1, 10 | 4 << 16);
            putChar('\t');
            printInt(cnt5, 10 | 4 << 16);
            putChar('\t');
            printInt(cnt10, 10 | 4 << 16);
            putChar('\r');
        }
    }

    return 0;
}
