#include <detpic32.h>

int main(void) { 
    // Configure ports, Timer T2, interrupts and external interrupt INT1 

    // Configure Timer T2 with interrupts enabled (frequencia = 2hz) 
    T2CONbits.TCKPS = 7; 
    PR2 = 39062; 
    TMR2 = 0; 
    T2CONbits.TON = 1;

    EnableInterrupts(); 
    while(1); 
    return 0; 
} 

void _int_(8) isr_T2(void){

} 

void _int_(7) isr_INT1(void){

} 
