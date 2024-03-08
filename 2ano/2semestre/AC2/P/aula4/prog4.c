#include <detpic32.h>

// Primeiro exercicio sobre o uso dos 7 segmentos;

int main(void){

    char c;

    // Registos RB8 a RB14 como OUTPUTS (1000 0000 1111 1111)
    TRISB = TRISB & 0x80FF;

    // Registos RD5 e RD6 como OUTPUTS (1111 1111 1001 1111)
    TRISD = TRISD & 0xFF9F;

    // Selecionar o DISPLAY menos significativo a partir dos enables (CL/RD5 e CH/RD6)
    LATDbits.LATD5 = 1;
    LATDbits.LATD6 = 0;

    while(1){
        c = getChar();
        
        if(c == 'a' || c == 'A') LATB = (LATB & 0x80FF) | 0x0100;
        else if(c == 'b' || c == 'B') LATB = (LATB & 0x80FF) | 0x0200;
        else if(c == 'c' || c == 'C') LATB = (LATB & 0x80FF) | 0x0400;
        else if(c == 'd' || c == 'D') LATB = (LATB & 0x80FF) | 0x0800;
        else if(c == 'e' || c == 'E') LATB = (LATB & 0x80FF) | 0x1000;
        else if(c == 'f' || c == 'F') LATB = (LATB & 0x80FF) | 0x2000;
        else if(c == 'g' || c == 'G') LATB = (LATB & 0x80FF) | 0x4000;
    }

    return 0;
}
