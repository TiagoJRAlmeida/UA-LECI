#include <detpic32.h>

void send2displays(unsigned char value) { 

    static const char display7Scodes[] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 
                                    0x7F, 0x6F, 0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71};

    
    // configure RB8-RB14 as outputs
    TRISB = TRISB & 0x80FF; // (1000 0000 1111 1111)

    // configure RD5-RD6 as outputs
    TRISD = TRISD & 0xFF9F; // (1111 1111 1001 1111)

    // static variable: doesn't loose its value between calls to function 
    static char displayFlag = 0; 
    digit_low = value & 0x0F; 
    digit_high = value >> 4; 

    // if "displayFlag" is 0 then send digit_low to display_low 
    // else send digit_high to didplay_high 
    if(displayFlag == 0){

        // Selecionar o display 'low'
        TRISDbits.TRISD5 = 0;
        TRISDbits.TRISD6 = 1;

        LATB = (LATB & 0x80FF) | digit_low << 8;

    }
    else if(displayFlag == 1){

        // Selecionar o display 'high'
        TRISDbits.TRISD5 = 1;
        TRISDbits.TRISD6 = 0;

        LATB = (LATB & 0x80FF) | digit_high << 8;

    }

    // toggle "displayFlag" variable
    !displayFlag; 
}
