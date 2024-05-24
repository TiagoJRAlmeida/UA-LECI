#include <detpic32.h>

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

void delay(unsigned int ms){
    resetCoreTimer();
    while(readCoreTimer() < (20000 * ms));
}

int main(void) { 
  // Taxa de transmissão/receção pretendida
  // U2BRG = (20000000/(16*115200)) - 1 = 9.85
  U2BRG = ((20000000 + 8*115200)/(16*115200)) - 1; 
  U2MODEbits.BRGH = 0; // 0 = 16; 1 = 4; 
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
    putstr("String de teste\n");
    // wait 1 s 
    delay(1000);
  } 

  return 0;
}
