#include <detpic32.h>
#include "/home/tiago/github/UA-LECI/2ano/2semestre/AC2/P/Functions.c"

// O programa deverá: 
// Timer T1: Fout = 5hz
// Kprescale = 20000000/TMRx; TMRx = 5hz * 65356; Kprescale = 20000000/(5 * 65356) = 61,2 --> 64
// PR1 = 20000000/(64 * 5) - 1 = 62499

// Timer T3: Fout = 100hz
// Kprescale = 20000000/TMRx; TMRx = 100hz * 65356; Kprescale = 20000000/(100 * 65356) = 3,1 --> 4
// PR3 = 20000000/(4 * 100) - 1 = 49999

// [1, 8, 64, 256]
// [1, 2, 4, 8, 16, 32, 64, 256]

volatile int voltage = 0; // Global variable

// Function to configure all (digital I/O, analog input, A/D module, 
// timers T1 and T3, interrupts) 
void configureAll(){
    unsigned int x = 4;
    unsigned int N = 8;
    TRISD = TRISD & 0xFF9F; // 1111 1111 1001 1111
    TRISB = TRISB & 0x80FF; // 1000 0000 1111 1111

    TRISBbits.TRISB4 = 1; 
    AD1PCFGbits.PCFG4 = 0; 
    AD1CON1bits.SSRC = 7; 
    AD1CON1bits.CLRASAM = 1;  
    AD1CON3bits.SAMC = 16;   
    AD1CON2bits.SMPI = N-1; 
    AD1CHSbits.CH0SA = x;   
    AD1CON1bits.ON = 1;

    IPC6bits.AD1IP = 2; // configure priority of A/D interrupts
    IEC1bits.AD1IE = 1;  // enable A/D interrupts 

    T1CONbits.TCKPS = 2;
    PR1 = 62499; 
    TMR1 = 0;    // Clear timer T1 count register 
    T1CONbits.TON = 1;

    T3CONbits.TCKPS = 2;
    PR3 = 49999; 
    TMR3 = 0;    // Clear timer T1 count register 
    T3CONbits.TON = 1;

    IPC1bits.T1IP = 2; // Interrupt priority (must be in range [1..6]) 
    IEC0bits.T1IE = 1; // Enable timer T1 interrupts 

    IPC3bits.T3IP = 2; // Interrupt priority (must be in range [1..6]) 
    IEC0bits.T3IE = 1; // Enable timer T3 interrupts 
}

int main(void) { 

    configureAll(); 
    // Reset AD1IF, T1IF and T3IF flags 
    IFS1bits.AD1IF = 0; 
    IFS0bits.T1IF = 0;
    IFS0bits.T3IF = 0; 

    EnableInterrupts();  // Global Interrupt Enable 
    while(1); 
    return 0; 
}

void _int_(4) isr_T1(void) { 
   // Start A/D conversion
    AD1CON1bits.ASAM = 1;

   // Reset T1IF flag 
   IFS0bits.T1IF = 0;
}

void _int_(12) isr_T3(void) { 
   // Send the value of the global variable "voltage" to the displays using BCD (decimal) format 
   send2displays(voltage);

   // Reset T3IF flag 
   IFS0bits.T3IF = 0; 
}

void _int_(27) isr_adc(void) { 
    // Calculate buffer average (8 samples)
    int i;
    voltage = 0;
    int* p = (int*)(&ADC1BUF0);
    for(i = 0; i < 16; i++){
        voltage += p[i*4];
    }
    voltage/=8;
    // Calculate voltage amplitude and copy it to "voltage" 
    voltage = (33*voltage + 511)/1023;
    voltage = toBcd(voltage);
    // Reset AD1IF flag 
    IFS1bits.AD1IF = 0;  
}
