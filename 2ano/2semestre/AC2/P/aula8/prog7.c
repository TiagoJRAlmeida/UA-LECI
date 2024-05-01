#include <detpic32.h>

void delay(unsigned int ms){
    resetCoreTimer();
    while(readCoreTimer() < (20000 * ms));
}

int main(void){

    // RD8 como INPUT
    TRISDbits.TRISD8 = 1;

    // RE0 como OUTPUT e inicializado com o valor 0;
    TRISEbits.TRISE0 = 0;
    LATEbits.LATE0 = 0;

    while(1){

        while(PORTDbits.RD8 == 0);
            LATEbits.LATE0 = 1;
            delay(3000);
            LATEbits.LATE0 = 0;
    } 

    return 0;
}
