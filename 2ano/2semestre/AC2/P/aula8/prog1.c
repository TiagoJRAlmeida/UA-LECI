#include <detpic32.h>


// Kprescaler = (Fpbclk)/((65535 + 1) * Fout) ==> Roof do valor obtido
// Com Fpbclk = 20 000 000 Hz e Fout = 2 Hz, temos:
// Kprescaler = roof de 152,587890625 = 153
// logo o prescaler será 256
// o novo PR3 = (20000000/256)/2 - 1 = 39062

// [1, 2, 4, 8, 16, 32, 64, 256]
int main(void) { 
    
    // Configure Timer T3 (2 Hz with interrupts disabled) 
    T3CONbits.TCKPS = 7; // 1:32 prescaler (i.e. fout_presc = 625 KHz) 
    PR3 = 39062; // Fout = 20MHz / (256 * (39062 + 1)) = 2 Hz 
    TMR3 = 0; // Clear timer T3 count register 
    T3CONbits.TON = 1; // Enable timer T3 (must be the last command of the timer configuration sequence)

    while(1) { 

        IPC3bits.T3IP = 2; // Interrupt priority (must be in range [1..6]) 
        IEC0bits.T3IE = 1; // Enable timer T3 interrupts 

        // Wait while T3IF = 0 
        while(IFS0bits.T3IF == 0);

        IFS0bits.T3IF = 0; // Reset timer T2 interrupt flag
        putChar('.'); 
    } 
    return 0; 
}
