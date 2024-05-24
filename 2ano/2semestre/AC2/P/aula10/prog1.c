#include <detpic32.h>

// Formulas:

// f_BRG = f_PBCLK / (UxBRG + 1)

// baudrate = f_PBCLK / (4 * (UxBRG + 1)) ou baudrate = f_PBCLK / (16 * (UxBRG + 1))

// UxBRG = (f_PBCLK / (16 * UxBRG )) - 1

// UxBRG = ((f_PBCLK + 8 * baudrate) / (16 * UxBRG )) - 1

void putc(char byte) { 
  // wait while UART2 UTXBF == 1
  while(U2STAbits.UTXBF == 1);
  // Copy "byte" to the U2TXREG register 
  U2TXREG = byte;
}

void delay(unsigned int ms){
    resetCoreTimer();
    while(readCoreTimer() < (20000 * ms));
}

int main(void) { 
  // Configure UART2: 
  // 1 - Configure BaudRate Generator 
  // 2 – Configure number of data bits, parity and number of stop bits 
  //     (see U2MODE register) 
  // 3 – Enable the trasmitter and receiver modules (see register U2STA) 
  // 4 – Enable UART2 (see register U2MODE) 

  // Taxa de transmissão/receção pretendida
  // U2BRG = (20000000/(16*115200)) - 1 = 9.85
  U2BRG = 10; 
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
    putc('+'); 
    // wait 1 s 
    delay(1000);
  } 

  return 0;
}
