#include <detpic32.h>

// U1 = 20000000/(16*115200) - 1 = 9.85

void putc1(char byte) { 
  // wait while UART1 UTXBF == 1 
  while(UART1bits.UTXBF == 1);
  // Copy "byte" to the U1TXREG register 
  U1TXREG = byte;
}

void delay(unsigned int ms){
    resetCoreTimer();
    while(readCoreTimer() < 20000 * ms);
}

int main(void){
    
    U1MODEbits.U1BRG = 10;
    U1MODEbits.BRGH = 0; // 0 = 16; 1 = 4;
    U1MODEbits.PDSEL = 1; // 0 = N; 1 = E; 2 = O;
    U1MODEbits.STSEL = 0;  // 0 = 1; 1 = 2;
    U1STAbits.UTXEN = 1;
    U1STAbits.URXEN = 1;
    U1MODEbits.ON = 1;

    while(1){
        putc1(0xA5);
        delay(10);
    }
    return 0;
}
