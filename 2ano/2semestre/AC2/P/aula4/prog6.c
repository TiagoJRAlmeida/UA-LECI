#include <detpic32.h>

// Mesmo exercicio que o prog5, agora para ver a diferença das frequencias;

// Delay de 10hz de frequencia
void delay(int ms){
    resetCoreTimer();
    while(readCoreTimer() < (ms * 20000));
}

int main(void){

    unsigned char segment;
    int i;
    int ctrl = 0; 
    int k=100;

    // Registos RB8 até RB14 como OUTPUT (1000 0000 1111 1111)
    TRISB = TRISB & 0x80FF;

    // Registos RD5 e RD6 como OUTPUT (1111 1111 1001 1111)
    TRISD = TRISD & 0xFF9F;

    // enable display low (RD5) and disable display high (RD6)
    LATDbits.LATD5 = 0;
    LATDbits.LATD6 = 1;

    while(1){
        segment = 1;

        if(ctrl == 2) k = 50;
        else if(ctrl == 4) k = 10;
        else if(ctrl == 6){ k = 100; ctrl = 0; }
        
        // LOOP COM FREQUENCIA VARIAVEL (10hz, 50hz, 100hz)
        for(i=0; i < 7; i++) {

            // send "segment" value to display
            LATB = (LATB & 0x80FF) | segment << 8;           

            delay(k);

            segment = segment << 1;
        }
        ctrl++;
        LATD = LATD ^0x0060; // (0000 0000 0110 0000)

    }    

    return 0;
}
