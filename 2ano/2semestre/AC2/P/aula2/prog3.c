#include <detpic32.h>

// 1hz = 1 segundo
// 5hz = 1/5 = 0,2 segundos
// 10hz = 1/10 = 0,1 segundos 

// 1 seg = delay(1000)
// 0.2 seg = delay(200)
// 0.1seg = delay(100)



void delay(unsigned int ms){
    resetCoreTimer();
    while(readCoreTimer() < 20000 * ms);
}

int main(void){
    int cnt1 = 0;
    int cnt5 = 0;
    int cnt10 = 0;

    while(1){
        delay(100);
        cnt10++;
        if(cnt10 >= 10 && cnt10 % 10 == 0){ cnt1++; }
        if(cnt10 >= 2 && cnt10 % 2 == 0) {cnt5++;}
        
        printInt(cnt1, 10 | 4 << 16);
        putChar('\t');
        printInt(cnt5, 10 | 4 << 16);
        putChar('\t');
        printInt(cnt10, 10 | 4 << 16);
        putChar('\r');
    }

    return 0;
}


