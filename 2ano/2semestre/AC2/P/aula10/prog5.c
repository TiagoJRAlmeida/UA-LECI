#include <detpic32.h>


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

void delay(unsigned int ms){
    resetCoreTimer();
    while(readCoreTimer() < (20000 * ms));
}

int main(void) { 
  // Configure UART2 (115200, N, 8, 1) 
  U2BRG = ((20000000 + 8*115200)/(16*115200)) - 1; 
  U2MODEbits.BRGH = 0; // Baudrate speed; 0 = 16; 1 = 4; 
  U2MODEbits.PDSEL = 0;  // Tipo de paridade; 0 = N; 1 = E; 2 = O; 3 = N;
  U2MODEbits.STSEL = 0; // Número de stop bits; 0 = 1; 1 = 2; 
  U2STAbits.UTXEN = 1; // Ativar o modulo de transmissão
  U2STAbits.URXEN = 1; // Ativar o modulo de receção
  U2MODEbits.ON = 1; // Ativar a UART

  while(1) { 
    // Read character using getc() 
    // Send character using putc() 
    putc(getc());
  } 

  return 0; 
} 

 