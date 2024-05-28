#include <detpic32.h>

// Timer T2: Freq = 120hz
// Kprescale = 20000000 / (65356 * 120) = 2.6 --> 4;
// PR2 = (20000000 / (4 * 120)) - 1 ~≃ 41666

// [1, 2, 4, 8, 16, 32, 64, 256]

void delay(unsigned int ms){
    resetCoreTimer();
    while(readCoreTimer() < (20000 * ms));
}

void send2displays(unsigned int value){
    static const char display7segcode[] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x67};

    static unsigned int displayFlag = 0;

    unsigned int lowDigit = value & 0x0F;
    unsigned int highDigit = value >> 4;

    if(displayFlag == 0){
        LATD = (LATD & 0xFF9F) | 0x0020;
        LATB = (LATB & 0x80FF) | display7segcode[lowDigit] << 8;
    }
    if(displayFlag == 1){
        LATD = (LATD & 0xFF9F) | 0x0040;
        LATB = (LATB & 0x80FF) | display7segcode[highDigit] << 8;
    }

    displayFlag = !displayFlag;
}

unsigned int toBcd(unsigned int value){
    return ((value / 10) << 4) + (value % 10);
}

volatile unsigned int voltage;

int main(void){
    unsigned int x = 4;
    unsigned int N = 2;
    

    TRISD = TRISD & 0xFF9F;
    TRISB = TRISB & 0x80FF;

    T2CONbits.TCKPS = 2; 
    PR2 = 41666;   
    TMR2 = 0;    
    T2CONbits.TON = 1;

    IPC2bits.T2IP = 2; 
    IEC0bits.T2IE = 1; 
    IFS0bits.T2IF = 0; 

    TRISBbits.TRISB4 = 1; 
    AD1PCFGbits.PCFG4 = 0; 
    AD1CON1bits.SSRC = 7; 
    AD1CON1bits.CLRASAM = 1;  
    AD1CON3bits.SAMC = 16;    
    AD1CON2bits.SMPI = N-1; 
    AD1CHSbits.CH0SA = x;   
    AD1CON1bits.ON = 1;

    EnableInterrupts();

    while(1){
        AD1CON1bits.ASAM = 1; 
        while(IFS1bits.AD1IF == 0);   

        int i;
        voltage = 0;
        int *p = (int*)(&ADC1BUF0);
        for(i = 0; i < 16; i++){
            voltage += p[i*4];
        }
        voltage /= 2;
        delay(100);
    }
     
}

void _int_(8) isr_T2(void){
    unsigned int temp = ((voltage*50)/1023) + 15;
    send2displays(toBcd(temp));
    IFS0bits.T2IF = 0; 
} 
