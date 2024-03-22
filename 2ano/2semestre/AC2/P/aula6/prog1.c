#include <detpic32.h>
#include "/home/tiago/github/UA-LECI/2ano/2semestre/AC2/P/Functions.c"

int main(void){

    unsigned int N = 1;
    unsigned int x = 4;

    // Desligar o OUTPUT digital de RB4;
    TRISBbits.TRISB4 = 1;

    // Ligar o INPUT analogico de RB4;
    AD1PCFGbits.PCFG4 = 0;

    AD1CON1bits.SSRC = 7; 
    AD1CON1bits.CLRASAM = 1;
    AD1CON3bits.SAMC = 16;     
    AD1CON2bits.SMPI = N-1;
    AD1CHSbits.CH0SA = x;
    AD1CON1bits.ON = 1;

    while(1) { 
    // Start conversion 
    AD1CON1bits.ASAM = 1;

    // Wait while conversion not done (AD1IF == 0) 
    while( IFS1bits.AD1IF == 0 );

    // Read conversion result (ADC1BUF0 value) and print it 
    printInt(ADC1BUF0, 16 | 3 << 16);
    putChar('\r');

    // Reset AD1IF 
    IFS1bits.AD1IF = 0;
    } 

    return 0;
}
