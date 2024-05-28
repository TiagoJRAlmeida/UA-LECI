#include <detpic32.h>
#include "/home/tiago/github/UA-LECI/2ano/2semestre/AC2/P/Functions.c"

// Timer 2 --> Freq 100hz:
// Kprescaler = 20000000 / (100 * 65356) --> 3.06 = 4
// PR2 = (20000000 / (100 * 4)) - 1 = 49999

// [1, 2, 4, 8, 16, 32, 64, 256]
// [1, 8, 64, 256]

volatile char c;
volatile unsigned char value;

void configureAll(){
    // RE0 - RE3 como OUTPUT
    TRISE = TRISE & 0xFFF0;
    
    // Enable dos displays como OUTPUT (RD5 e RD6)
    TRISD = TRISD & 0xFF9F;
    // Displays como OUTPUT (RB8-RB14)
    TRISB = TRISB & 0x80FF;

    // Configurar o timer 2 e interupção do mesmo (freq = 100hz)
    T2CONbits.TCKPS = 2; 
    PR2 = 49999;   
    TMR2 = 0;    
    T2CONbits.TON = 1; 
            
    IPC2bits.T2IP = 2;
    IEC0bits.T2IE = 1;     
}

int main(void){

    configureAll();
    
    IFS0bits.T2IF = 0; 
    LATE = LATE & 0xFFF0;
    EnableInterrupts();
    while(1){
        c = inkey();
        if (c == '0') {
            LATE = (LATE & 0xFFF0) | 0x0001;
            value = 0;
        } 
        else if (c == '1') {
            LATE = (LATE & 0xFFF0) | 0x0002;
            value = 1;
        } 
        else if (c == '2') {
            LATE = (LATE & 0xFFF0) | 0x0004;
            value = 2;
        } 
        else if (c == '3') {
            LATE = (LATE & 0xFFF0) | 0x0008;
            value = 3;
        } 
        else if(c != 0x00){
            LATE = (LATE & 0xFFF0) | 0x000F;
            value = 255;
            delay(1000);
            LATE = LATE & 0xFFF0;
            value = 4;
        }
    };

    return 0;
}

void _int_(8) isr_T2(void) { 
    if(value != 4)
        send2displays(value);
    else{
        LATD = (LATD & 0xFF9F) | 0x0020;
        LATB = LATB & 0x80FF;
        LATD = (LATD & 0xFF9F) | 0x0040;
        LATB = LATB & 0x80FF;
    }    
        
    // reset flag
    IFS0bits.T2IF = 0;
}