#include <detpic32.h>
#include "/home/tiago/github/UA-LECI/2ano/2semestre/AC2/P/Functions.c"

// O programa deverá: 
// i) efetuar 5 sequências de conversão A/D por segundo (frequência de amostragem de 5 Hz), cada uma delas com 4 amostras; 
// ii) enviar informação para o sistema de visualização a cada 10 ms (frequência de refrescamento de 100 Hz);

int main(void) { 
    
    unsigned int x = 4;
    unsigned int N = 4;
    unsigned int i;
    unsigned int average;
    unsigned int tensao = 0;

    // Desligar o OUTPUT digital de RB4;
    TRISBbits.TRISB4 = 1;

    // Ligar o INPUT analogico de RB4;
    AD1PCFGbits.PCFG4 = 0;

    // Ligar o OUTPUT do enable dos displays
    TRISD = TRISD & 0xFF9F; // (1111 1111 1001 1111) 

    // Ligar o OUTPUT dos displays (RB8 - RB14)
    TRISB = TRISB & 0x80FF; // (1000 0000 1111 1111)

    AD1CON1bits.SSRC = 7; 
    AD1CON1bits.CLRASAM = 1;
    AD1CON3bits.SAMC = 16;     
    AD1CON2bits.SMPI = N-1;
    AD1CHSbits.CH0SA = x;
    AD1CON1bits.ON = 1;

    i = 0; 
    while(1) { 
        if(i == 0) {  // 0, 200ms, 400ms, 600ms, ... 
         
            // reset average
            average = 0;

            // Convert analog input (4 samples) 

            // Start conversion 
            AD1CON1bits.ASAM = 1;

            // Wait while conversion not done (AD1IF == 0) 
            while( IFS1bits.AD1IF == 0 );

            int *p = (int *)(&ADC1BUF0); 

            // Read samples and calculate the average
            for( i = 0; i < 4; i++ ) { 
                average += p[i*4];
            }
            average /= 4;

            // Calculate voltage amplitude 
            tensao = (average*33 + 511) / 1023; 

            // Convert voltage amplitude to decimal
            tensao = toBcd(tensao);
        } 

        // Send voltage value to displays
        send2displays(tensao);

        // Wait 10 ms (using the core timer) 
        delay(10);

        i = (i + 1) % 20; 
    } 
    return 0; 
}
