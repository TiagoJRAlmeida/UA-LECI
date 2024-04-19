#include <detpic32.h>

int main(void){

    // portos RE1 e RE3 como saídas
    TRISEbits.TRISE1 = 0;
    TRISEbits.TRISE3 = 0;

    // Inicialize-os com o valor lógico 0
    LATD = LATD & 0xFFF5; // 1111 1111 1111 0101

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
    LATEbits.LATE1 = !LATEbits.LATE1;
    // Reset T3 interrupt flag 
    IFS0bits.T1IF = 0;
}

void _int_(12) isr_T3(void) { // Replace VECTOR by the timer T3 vector number
    LATEbits.LATE3 = !LATEbits.LATE3;
    // Reset T3 interrupt flag 
    IFS0bits.T3IF = 0;
}
