#include <detpic32.h>

void send2displays(unsigned char value) { 
    static const char display7Scodes[] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 
                                    0x7F, 0x6F, 0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71};
    unsigned char dh, dl; 

    // Indicar RB8 - RB14 como OUTPUTS
    TRISB = TRISB & 0x80FF; // (1000 0000 1111 1111)

    // Indicar RD5 e RD6 como OUTPUTS
    TRISD = TRISD & 0xFF9F; // (1111 1111 1001 1111)

    // select display high 
    TRISDbits.TRISD5 = 1;
    TRISDbits.TRISD6 = 0;

    // send digit_high (dh) to display: dh = value >> 4
    dh = value >> 4;
    LATB = (LATB & 0x80FF) | display7Scodes[dh] << 8;  

    // select display low 
    TRISDbits.TRISD5 = 0;
    TRISDbits.TRISD6 = 1;

    // send digit_low (dl) to display:  dl = value & 0x0F
    dl = value & 0x0F;
    LATB = (LATB & 0x80FF) | display7Scodes[dl] << 8; 

}
 