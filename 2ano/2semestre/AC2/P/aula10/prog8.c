#include <detpic32.h>

// U2 = 20000000/(16*115200) - 1 = 9.85

char getc(void){ 
  // Wait while URXDA == 0 
  while(U2STAbits.URXDA == 0);
  // Return U2RXREG 
  return U2RXREG;
}

void putc(char byte) { 
  while(U2STAbits.UTXBF == 1);
  U2TXREG = byte;
}

void putstr(char *str) { 
  while(*str != '\0'){
    putc(*str);
    str++; 
  }
}

int main(void) { 
    // Configure UART2 (115200, N, 8, 1) 
    U2BRG = 10;
    U2MODEbits.BRGH = 0; // 0 = 16; 1 = 4;
    U2MODEbits.PDSEL = 0; // 0 = N; 1 = E; 2 = O;
    U2MODEbits.STSEL = 0;  // 0 = 1; 1 = 2;
    U2STAbits.UTXEN = 1;
    U2STAbits.URXEN = 1;
    U2MODEbits.ON = 1;

    // config RD11 as output
    TRISDbits.TRISD11 = 0;

    while(1){ 
        // Wait while TRMT == 0
        while(U2STAbits.TRMT == 0); 
        // Set RD11 
        LATDbits.LATD11 = 1;
        putstr("123456789AB"); 
        // Reset RD11
        LATDbits.LATD11 = 0; 
    } 
    return 0; 
}