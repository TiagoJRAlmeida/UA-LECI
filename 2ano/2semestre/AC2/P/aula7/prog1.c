#include <detpic32.h>

int main(void) {
    unsigned int x = 4;
    unsigned int N = 4;

    // Configure all (digital I/O, analog input, A/D module) 
    TRISBbits.TRISB4 = 1; // RBx digital output disconnected 
    AD1PCFGbits.PCFG4= 0; // RBx configured as analog input 
    AD1CON1bits.SSRC = 7; // Conversion trigger selection bits: in this mode an internal counter ends sampling and starts conversion 
    AD1CON1bits.CLRASAM = 1;  // Stop conversions when the 1st A/D converter interrupt is generated. At the same time, hardware clears the ASAM bit 
    AD1CON3bits.SAMC = 16;    // Sample time is 16 TAD (TAD = 100 ns) 
    AD1CON2bits.SMPI = N-1; // Interrupt is generated after N samples (replace N by the desired number of consecutive samples) 
    AD1CHSbits.CH0SA = x;   // replace x by the desired input analog channel (0 to 15) 
    AD1CON1bits.ON = 1; 

    // Configure interrupt system 
    IPC6bits.AD1IP = 2;  // configure priority of A/D interrupts 
    IFS1bits.AD1IF = 0;  // clear A/D interrupt flag 
    IEC1bits.AD1IE = 1;  // enable A/D interrupts 

    EnableInterrupts();    // Global Interrupt Enable 

    // Start A/D conversion 
    AD1CON1bits.ASAM = 1;

    while(1);      // all activity is done by the ISR 
    return 0; 
}


void _int_(27) isr_adc(void) { 
  // Read conversion result (ADC1BUF0) and print it 
  int i;
  int *p = (int*)(&ADC1BUF0);
  for(i = 0; i < 16; i++){
    printInt10(p[i*4]);
    putChar(' ');
  }
  putChar('\r');
  
  AD1CON1bits.ASAM = 1; // Start A/D conversion 
  IFS1bits.AD1IF = 0;   // Reset AD1IF flag 
}