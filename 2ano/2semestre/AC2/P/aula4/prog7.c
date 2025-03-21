#include <detpic32.h>

void delay(int ms){
    resetCoreTimer();
    while(readCoreTimer() < (ms * 20000));
}

int main(void){
    
    // -GFE DCBA
    // 0000 0000   
    // 0 : 0011 1111 : 0x3F
    // 1 : 0000 0110 : 0x06
    // 2 : 0101 1011 : 0x5B
    // 3 : 0100 1111 : 0x4F
    // 4 : 0110 0110 : 0x66
    // 5 : 0110 1101 : 0x6D
    // 6 : 0111 1101 : 0x7D
    // 7 : 0000 0111 : 0x07
    // 8 : 0111 1111 : 0x7F
    // 9 : 0110 1111 : 0x6F
    // A : 0111 0111 : 0x77
    // b : 0111 1100 : 0x7C
    // c : 0011 1001 : 0x39
    // d : 0101 1110 : 0x5E
    // E : 0111 1001 : 0x79
    // F : 0111 0001 : 0x71

    int disp7Scodes[] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 
                    0x7F, 0x6F, 0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71}; 

    int i;

    // Registos RB8 até RB14 como OUTPUT (1000 0000 1111 1111)
    TRISB = TRISB & 0x80FF;

    // Registos RD5 e RD6 como OUTPUT (1111 1111 1001 1111)
    TRISD = TRISD & 0xFF9F;

    // enable display low (RD5) and disable display high (RD6)
    LATDbits.LATD5 = 0;
    LATDbits.LATD6 = 1;

    while(1){
        for(i = 0; i < 16; i++){
            
            LATB = (LATB & 0x80FF) | disp7Scodes[i] << 8;

            delay(1000);
        }
    }   

    return 0;
}
