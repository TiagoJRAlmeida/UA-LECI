#include <detpic32.h>

int main(void) { 
   
    static const char disp7Scodes[] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 
                                    0x7F, 0x6F, 0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71}; 
   
    // configure RB0 to RB3 as inputs
    TRISB = TRISB | 0x000F;  

    // configure RB8 to RB14 and RD5 to RD6 as outputs
    TRISB = TRISB & 0x80FF;  // (1000 0000 1111 1111)
    TRISD = TRISD & 0xFF9F;

    // Select display low 
    LATDbits.LATD5 = 1;
    LATDbits.LATD6 = 0;

    while(1) { 
        int ds;

        // read dip-switch
        ds = PORTB & 0x000F; // 0000 0000 0000 1111

        // convert to 7 segments code 
        LATB = (LATB & 0x80FF) | disp7Scodes[ds] << 8;

        // send to display 
    } 

    return 0; 
} 
