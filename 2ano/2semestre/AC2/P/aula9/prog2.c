#include <detpic32.h>

// Timer T3: Fout = 100hz
// Kprescale = 20000000/(65356 * 100) = 3,1 --> 4
// PR3 = 20000000/(4*100) - 1 = 49999


// Duty-cycle de 25%:
// OC1RS = 50000*0.25 = 12500
// Resolução = log2((20000000/4)/100) = 15,6 --> 15 bits

// [1, 2, 4, 8, 16, 32, 64, 256]
// [1, 8, 64, 256]

void setPWM(unsigned int dutyCycle) { 
  // duty_cycle must be in the range [0, 100]
  if(dutyCycle < 0 || dutyCycle > 100) return;
  OC1RS = (50000*dutyCycle)/100; // Determine OC1RS as a function of "dutyCycle" 
}

int main(void){

    TRISCbits.TRISC14 = 0;

    T3CONbits.TCKPS = 2; 
    PR3 = 49999;  
    TMR3 = 0;  
    T3CONbits.TON = 1; 

    IPC3bits.T3IP = 2; 
    IEC0bits.T3IE = 1; 
    IFS0bits.T3IF = 0; 

    OC1CONbits.OCM = 6;  // PWM mode on OCx; fault pin disabled 
    OC1CONbits.OCTSEL = 1;  // Use timer T3 as the time base for PWM generation 
    OC1RS = 12500; // Ton constant 
    OC1CONbits.ON = 1; // Enable OC1 module
 
    EnableInterrupts();
    while(1){
      char c =inkey();
      if(c == '1'){
        setPWM(5);
      } 
      else if(c == '2'){
        setPWM(90);
      }
      LATCbits.LATC14 = PORTDbits.RD0; 
    }

    return 0;
}

void _int_(12) isr_T3(void) { 
    LATDbits.LATD0 = 1;
    // Reset T3IF flag 
    IFS0bits.T3IF = 0;   
}
