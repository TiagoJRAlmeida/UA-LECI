#include <detpic32.h>
#include "/home/tiago/github/UA-LECI/2ano/2semestre/AC2/P/Functions.c"

int main(void){

    unsigned int N = 4;
    unsigned int x = 4;
    unsigned int i;
    unsigned int average;
    unsigned int tensao;

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

        // reset average 
        average = 0; 

        // Start conversion 
        AD1CON1bits.ASAM = 1;

        // Wait while conversion not done (AD1IF == 0) 
        while( IFS1bits.AD1IF == 0 );
        putChar('\r');

        int *p = (int *)(&ADC1BUF0); 

        for( i = 0; i < 16; i++ ) { 

            // Read conversion result (ADC1BUF0 value) and print it 
            printInt( p[i*4], 10 | 4 << 16 ); 
            putChar(' ');
            average += p[i*4];
        }

        average /= 4;
        tensao = (average*33 + 511) / 1023;
        printStr("Voltagem: ");
        printInt(tensao, 10);
        printStr(" dV");

        // Reset AD1IF 
        IFS1bits.AD1IF = 0;

    } 

    return 0;
}
