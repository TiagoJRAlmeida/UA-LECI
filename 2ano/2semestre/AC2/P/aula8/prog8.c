#include <detpic32.h>


static int counter = 0; 

int main(void) { 
    // Configure ports, Timer T2, interrupts and external interrupt INT1 
    TRISDbits.TRISD8 = 1;

    // Configure Timer T2 with interrupts enabled (frequencia = 2hz) 
    T2CONbits.TCKPS = 7; 
    PR2 = 39062; 
    TMR2 = 0; 
    // T2CONbits.TON = 1;

    // RE0 como OUTPUT e inicializado com o valor 0;
    TRISEbits.TRISE0 = 0;
    LATEbits.LATE0 = 0;

    // Configurar INT1 como falling edge
    INTCONbits.INT1EP = 0;

    EnableInterrupts();

    IPC2bits.T2IP = 2; // Interrupt priority (must be in range [1..6]) 
    IEC0bits.T2IE = 1; // Enable timer T2 interrupts  

    IPC1bits.INT1IP = 2;
    IEC0bits.INT1IE = 1;
    while(1); 
    return 0; 
} 

void _int_(8) isr_T2(void){
    counter++;
    if(counter == 5){
        counter = 0;
        LATEbits.LATE0 = 0;
        T2CONbits.TON = 0;
    }
    // Reset T2 interrupt flag 
    IFS0bits.T2IF = 0;  
} 

void _int_(7) isr_INT1(void){
    LATEbits.LATE0 = 1;
    T2CONbits.TON = 1;
    IFS0bits.INT1IF = 0;
} 
