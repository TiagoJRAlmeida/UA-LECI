#include <detpic32.h>

// Igual ao prog1.c, mas com fator de sobreamostragem de 4.
void putc(char byte) { 
  while(U2STAbits.UTXBF == 1);
  U2TXREG = byte;
}

void delay(unsigned int ms){
    resetCoreTimer();
    while(readCoreTimer() < (20000 * ms));
}

int main(void) { 
  // Taxa de transmissão/receção pretendida
  // U2BRG = (20000000/(4*115200)) - 1 = 42.40
  U2BRG = 42; 
  U2MODEbits.BRGH = 1; // 0 = 16; 1 = 4; 
  // Tipo de paridade
  U2MODEbits.PDSEL = 0;  // sem paridade, 8 data bits
  // Número de stop bits
  U2MODEbits.STSEL = 0; // 1 stop bit
  // Ativar o modulo de transmissão
  U2STAbits.UTXEN = 1;
  // Ativar o modulo de receção
  U2STAbits.URXEN = 1;
  // Ativar a UART
  U2MODEbits.ON = 1;

  while(1){ 
    putc('+'); 
    // wait 1 s 
    delay(1000);
  } 

  return 0;
}
