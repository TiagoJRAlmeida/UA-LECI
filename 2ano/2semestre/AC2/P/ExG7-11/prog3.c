#include <detpic32.h>

// Timer T3: Freq = 1khz
// Kprescale = 20000000/(65356 * 1000) = 0.3 --> 1
// PR3 = (20000000/(1 * 1000)) - 1 = 19999

void setPWM(unsigned int dutyCycle){
    if(dutyCycle > 100) return;
    OC3RS = 19999 * dutyCycle/100; 
}

int main(void){
    unsigned int x = 4;
    unsigned int N = 4;
    unsigned int i;
    unsigned int voltage;
    unsigned int newDutyCycle;

    TRISCbits.TRISC14 = 0;

    T3CONbits.TCKPS = 0; 
    PR3 = 19999;  
    TMR3 = 0;    
    T3CONbits.TON = 1;

    OC3CONbits.OCM = 6;  
    OC3CONbits.OCTSEL = 1;
    setPWM(25);   
    OC3CONbits.ON = 1;

    TRISBbits.TRISB4 = 1; 
    AD1PCFGbits.PCFG4= 0;
    AD1CON1bits.SSRC = 7; 
    AD1CON1bits.CLRASAM = 1; 
    AD1CON3bits.SAMC = 16;   
    AD1CON2bits.SMPI = N-1; 
    AD1CHSbits.CH0SA = x;  
    AD1CON1bits.ON = 1;    

    while(1){
        voltage = 0;
        newDutyCycle = 0;
        AD1CON1bits.ASAM = 1;
        while( IFS1bits.AD1IF == 0 );
        int *p = (int*)(&ADC1BUF0);
        for(i = 0; i < 16; i++){
            voltage += p[i*4];
        }
        voltage /= 4;
        newDutyCycle = (voltage * 100 + 511)/1023;
        printInt10(voltage);
        printStr("    ");
        printInt10(newDutyCycle);
        putChar('\r');
        setPWM(newDutyCycle);
        LATCbits.LATC14 = PORTDbits.RD2;
        resetCoreTimer();
        while(readCoreTimer() < 2000000);
    }

    return 0;
}
