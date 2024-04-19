#include <detpic32.h>


// Kprescaler = (Fpbclk)/((65535 + 1) * Fout) ==> Roof do valor obtido
// Com Fpbclk = 20 000 000 Hz e Fout = 2 Hz, temos:
// Kprescaler = roof de 152,587890625 = 153
// logo o prescaler será 256
// o novo PR3 = (20000000/256)/2 - 1 = 39062

// [1, 2, 4, 8, 16, 32, 64, 256]

static int counter = 0;

int main(void) { 
    // Configure Timer T3 with interrupts enabled 
    T3CONbits.TCKPS = 7; 
    PR3 = 39062; 
    TMR3 = 0; 
    T3CONbits.TON = 1;

    EnableInterrupts(); 
    IPC3bits.T3IP = 2; // Interrupt priority (must be in range [1..6]) 
    IEC0bits.T3IE = 1; // Enable timer T3 interrupts 
    while(1); 

    return 0;
}


void _int_(12) isr_T3(void) { // Replace VECTOR by the timer T3 vector number
    counter++;
    if(counter == 2) {
        counter = 0;
        putChar('.');
    } 
    // Reset T3 interrupt flag 
    IFS0bits.T3IF = 0;
}
