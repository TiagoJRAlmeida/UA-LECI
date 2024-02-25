#include <detpic32.h>

// 1hz = 1 segundo
// 5hz = 1/5 = 0,2 segundos
// 10hz = 1/10 = 0,1 segundos 

void delay(unsigned int ms){
    resetCoreTimer();
    while(readCoreTimer() < 2000000 * ms);
}

int main(void) { 
    int counter = 0; 
    while(1) { 
        putChar('\r');  // cursor regressa ao inicio da linha no ecrã 
        printInt(counter, 10 | 4 << 16); // Ver nota de rodapé 1 
        resetCoreTimer(); 
        while(readCoreTimer() < 200000); 
        counter++; 
    } 
    return 0; 
}

// int main(void){
//     int cnt1 = 0;
//     int cnt5 = 0;
//     int cnt10 = 0;

//     while(1){
//         delay(1);
//         cnt10++;
//         if(cnt10 < 10) continue;
//         else
//             if(cnt10 % 2 == 0) cnt5++;
//             if(cnt10 % 10 == 0) cnt1++;
//         printf("%5d   %5d   %5d", cnt1, cnt5, cnt10);
//         putchar("\r");
//     }
// }
