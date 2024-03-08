#include <detpic32.h>

// Delay de 2hz de frequencia
void delay(){
    resetCoreTimer();
    while(readCoreTimer() < 10000000);
}

int main(void){

    unsigned char segment;

    // Registos RB8 até RB14 como OUTPUT (1000 0000 1111 1111)
    TRISB = TRISB & 0x80FF;

    // Registos RD5 e RD6 como OUTPUT (1111 1111 1001 1111)
    TRISD = TRISD & 0xFF9F;

    // enable display low (RD5) and disable display high (RD6)
    LATDbits.LATD5 = 0;
    LATDbits.LATD6 = 1;

    while(1){
        segment = 1;
        int i;
        for(i=0; i < 7; i++) {

            // send "segment" value to display
            LATB = (LATB & 0x80FF) | segment << 8;           

            // wait 0.5 second
            delay();

            segment = segment << 1;
        }

        LATD = LATD ^0x0060; // (0000 0000 0110 0000)
    }

    

    return 0;
}
