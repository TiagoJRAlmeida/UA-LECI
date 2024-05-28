#include <detpic32.h>

// Timer T2: Freq = 150hz
// Kprescaler = 20000000 / (65356 * 150) = 2.04 --> 4
// PR2 = (20000000 / (4 * 150)) - 1 = 33332.3

// [1, 2, 4, 8, 16, 32, 64, 256]

void setPWM(unsigned int dutyCycle){
    if(dutyCycle > 100) return;
    OC2RS = (33333 * dutyCycle)/100;
}

int main(void){
    TRISB = TRISB | 0x0009; // 0000 0000 0000 1001
    TRISCbits.TRISC14 = 0;

    T2CONbits.TCKPS = 2;
    PR2 = 33332;  
    TMR2 = 0;    
    T2CONbits.TON = 1;

    OC2CONbits.OCM = 6;  
    OC2CONbits.OCTSEL = 0; 
    OC2RS = 8333;
    OC2CONbits.ON = 1; 

    while(1){
        if(PORTBbits.RB3 == 0 && PORTBbits.RB0 == 1){ 
            setPWM(25); 
        }
        else if(PORTBbits.RB3 == 1 && PORTBbits.RB0 == 0){ 
            setPWM(70);
        }
        resetCoreTimer();
        while(readCoreTimer() < 50000);
        LATCbits.LATC14 = PORTDbits.RD1;
    }

    return 0;
}
