#include <detpic32.h>

// Timer 1 --> Freq = 10hz
// Kprescale = 20000000/(65356*10) = 30.6 --> 64
// PR1 = (20000000/(64*10)) - 1 = 31249

// Timer 2 --> Freq = 50hz
// Kprescale = 20000000/(65356*50) = 6.1 --> 8
// PR1 = (20000000/(8*50)) - 1 = 49999

// [1, 2, 4, 8, 16, 32, 64, 256]
// [1, 8, 64, 256]

volatile unsigned int counter = 0;

void send2displays(unsigned char value){
    static const char display7Scodes[] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 
                                    0x7F, 0x6F, 0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71};
    unsigned char digit_low, digit_high;
    digit_low = value & 0x0F;
    digit_high = value >> 4;

    static char displayFlag = 0;

    if(displayFlag == 0){
        LATD = (LATD & 0xFF9F) | 0x0020;
        LATB = (LATB & 0x80FF) | display7Scodes[digit_low] << 8; 
    }

    if(displayFlag == 1){
        LATD = (LATD & 0xFF9F) | 0x0040;
        LATB = (LATB & 0x80FF) | display7Scodes[digit_high] << 8; 
    }

    displayFlag = !displayFlag;

}

unsigned char toBcd(unsigned char value){
    return ((value/10) << 4) | (value % 10);
}

void configureAll(){

    // Configure displays enables as OUTPUT (RD5-RD6)
    TRISD = TRISD & 0xFF9F;
    // Configure displays as OUTPUT (RB8-RB14)
    TRISB = TRISB & 0x80FF;

    // Configure T1
    T1CONbits.TCKPS = 2; 
    PR1 = 31249;   
    TMR1 = 0;     
    T1CONbits.TON = 1;

    IPC1bits.T1IP = 2; 
    IEC0bits.T1IE = 1;

    // Configure T2
    T2CONbits.TCKPS = 3; 
    PR2 = 49999;   
    TMR2 = 0;    
    T2CONbits.TON = 1;

    IPC2bits.T2IP = 2; 
    IEC0bits.T2IE = 1;
}

int main(void){

    configureAll();
    IFS0bits.T1IF = 0;
    IFS0bits.T2IF = 0;

    EnableInterrupts();

    while(1);

    return 0;
}

void _int_(4) isr_T1(void) { 
    counter = (counter + 1) % 100;
    printInt(counter, 16 | 2 << 16);
    putChar('\n');

    IFS0bits.T1IF = 0;  
}

void _int_(8) isr_T2(void) { 
    send2displays(toBcd(counter));

    IFS0bits.T2IF = 0;  
}