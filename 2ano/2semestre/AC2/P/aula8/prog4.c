#include <detpic32.h>

// Teoria para o Timer 1:
// Kprescaler = (Fpbclk)/((65535 + 1) * Fout) ==> Roof do valor obtido
// Com Fpbclk = 20 000 000 Hz e Fout = 5 Hz, temos:
// Kprescaler = roof de 61,03515625 = 64
// logo o prescaler será 64
// o novo PR3 = (20000000/64)/5 - 1 = 62499

// Teoria para o Timer 3:
// Kprescaler = (Fpbclk)/((65535 + 1) * Fout) ==> Roof do valor obtido
// Com Fpbclk = 20 000 000 Hz e Fout = 25 Hz, temos:
// Kprescaler = roof de 12,20703125 = 13
// logo o prescaler será 16
// o novo PR3 = (20000000/16)/25 - 1 = 49999


// [1, 8, 64, 256]
// [1, 2, 4, 8, 16, 32, 64, 256]


int main(void) { 

    // Configure Timer T1 with interrupts enabled  (frequencia = 5hz)
    T1CONbits.TCKPS = 2; 
    PR1 = 62499; 
    TMR1 = 0; 
    T1CONbits.TON = 1;

    // Configure Timer T3 with interrupts enabled (frequencia = 25hz)
    T3CONbits.TCKPS = 4; 
    PR3 = 49999; 
    TMR3 = 0; 
    T3CONbits.TON = 1;

    EnableInterrupts(); 
    IPC1bits.T1IP = 2; // Interrupt priority (must be in range [1..6]) 
    IEC0bits.T1IE = 1; // Enable timer T1 interrupts 
    
    IPC3bits.T3IP = 2; // Interrupt priority (must be in range [1..6]) 
    IEC0bits.T3IE = 1; // Enable timer T3 interrupts 
    while(1); 

    return 0;
}


void _int_(4) isr_T1(void) { // Replace VECTOR by the timer T1 vector number
    putChar('1');
    putChar('\n');
    // Reset T3 interrupt flag 
    IFS0bits.T1IF = 0;
}

void _int_(12) isr_T3(void) { // Replace VECTOR by the timer T3 vector number
    putChar('3');
    // Reset T3 interrupt flag 
    IFS0bits.T3IF = 0;
}
