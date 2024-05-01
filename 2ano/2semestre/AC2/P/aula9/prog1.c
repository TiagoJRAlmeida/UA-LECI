#include <detpic32.h>
#include "/home/tiago/github/UA-LECI/2ano/2semestre/AC2/P/Functions.c"

// O programa deverá: 
// i) efetuar 5 sequências de conversão A/D por segundo (frequência de amostragem de 5 Hz), cada uma delas com 4 amostras; 
// ii) enviar informação para o sistema de visualização a cada 10 ms (frequência de refrescamento de 100 Hz);

// TIMER 1 TEORIA:
// Kprescaler = (Fpbclk)/((65535 + 1) * Fout) ==> Roof do valor obtido
// Com Fpbclk = 20 000 000 Hz e Fout = 5 Hz, temos:
// Kprescaler = roof de 61,03515625 = 64
// logo o prescaler será 64
// o novo PR1 = (20000000/64)/5 - 1 = 62499

// TIMER 3 TEORIA:
// Kprescaler = (Fpbclk)/((65535 + 1) * Fout) ==> Roof do valor obtido
// Com Fpbclk = 20 000 000 Hz e Fout = 100 Hz, temos:
// Kprescaler = roof de 3,051757812 = 4
// logo o prescaler será 4
// o novo PR3 = (20000000/4)/100 - 1 = 49999

// [1, 8, 64, 256]
// [1, 2, 4, 8, 16, 32, 64, 256]


int main(void) { 
    
    unsigned int x = 4;
    unsigned int N = 4;
    unsigned int i;


    // Desligar o OUTPUT digital de RB4;
    TRISBbits.TRISB4 = 1;

    // Ligar o INPUT analogico de RB4;
    AD1PCFGbits.PCFG4 = 0;

    // Ligar o OUTPUT do enable dos displays
    TRISD = TRISD & 0xFF9F; // (1111 1111 1001 1111) 

    // Ligar o OUTPUT dos displays (RB8 - RB14)
    TRISB = TRISB & 0x80FF; // (1000 0000 1111 1111)

    // Configure Timer T1 with interrupts enabled  (frequencia = 5hz)
    T1CONbits.TCKPS = 2; 
    PR1 = 62499; 
    TMR1 = 0; 
    T1CONbits.TON = 1;

    // Configure Timer T3 with interrupts enabled (frequencia = 100hz)
    T3CONbits.TCKPS = 2; 
    PR3 = 49999; 
    TMR3 = 0; 
    T3CONbits.TON = 1;

    AD1CON1bits.SSRC = 7; 
    AD1CON1bits.CLRASAM = 1;
    AD1CON3bits.SAMC = 16;     
    AD1CON2bits.SMPI = N-1;
    AD1CHSbits.CH0SA = x;
    AD1CON1bits.ON = 1;

    // Reset AD1IF, T1IF and T3IF flags 
    EnableInterrupts();  // Global Interrupt Enable 
    IPC1bits.T1IP = 2; // Interrupt priority (must be in range [1..6]) 
    IEC0bits.T1IE = 1; // Enable timer T1 interrupts 
    
    IPC3bits.T3IP = 2; // Interrupt priority (must be in range [1..6]) 
    IEC0bits.T3IE = 1; // Enable timer T3 interrupts 
    while(1); 
    return 0; 
}

void _int_(4) isr_T1(void) { 
    // Start A/D conversion 
    AD1CON1bits.ASAM = 1;

    // Wait while conversion not done (AD1IF == 0) 
    //while( IFS1bits.AD1IF == 0 );

   // Reset T1IF flag
    IFS0bits.T1IF = 0;
}

void _int_(12) isr_T3(void) { 
    // Send the value of the global variable "voltage" to the displays 
    //  using BCD (decimal) format 
    int average = 0;
    int tensao = 0;
    int *p = (int *)(&ADC1BUF0); 
    int i = 0;
    // Read samples and calculate the average
    for( i = 0; i < 4; i++ ) { 
        average += p[i*4];
    }
    average /= 4;

    // Calculate voltage amplitude 
    tensao = (average*33 + 511) / 1023; 

    // Convert voltage amplitude to decimal
    tensao = toBcd(tensao);

    // Send voltage value to displays
    send2displays(tensao);

    // Reset T3IF flag
    IFS0bits.T3IF = 0;
}
