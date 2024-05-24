#include <detpic32.h>

// <********** CONTEXTO ***********> 
// MESMO EXERCICIO QUE O prog6.c (o exercicio 7 da parte 1) 
// MAS A TRANSFORMAÇÃO PARA BINARIO É DIFERENTE.
char getc(void){ 
  while(U2STAbits.URXDA == 0);
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

void delay(unsigned int ms){
    resetCoreTimer();
    while(readCoreTimer() < (20000 * ms));
}

void intToBinary(int value, char* buffer) {
    int i;
    for(i = 4; i >= 0; i--) {
        buffer[4-i] = (value & (1 << i)) ? '1' : '0';
    }
    buffer[5] = '\0'; 
}

static unsigned int counter = 0;

int main(void) { 
  // Configure UART2 (115200, N, 8, 1) 
  U2BRG = ((20000000 + 2*115200)/(4*115200)) - 1; 
  U2MODEbits.BRGH = 1; // Baudrate speed; 0 = 16; 1 = 4; 
  U2MODEbits.PDSEL = 0;  // Tipo de paridade; 0 = N; 1 = E; 2 = O; 3 = N;
  U2MODEbits.STSEL = 0; // Número de stop bits; 0 = 1; 1 = 2; 
  U2STAbits.UTXEN = 1; // Ativar o modulo de transmissão
  U2STAbits.URXEN = 1; // Ativar o modulo de receção
  U2MODEbits.ON = 1; // Ativar a UART

  // Configure Timer T3 with interrupts enabled 
    T3CONbits.TCKPS = 6; 
    PR3 = 62499; 
    TMR3 = 0; 
    T3CONbits.TON = 1;

    EnableInterrupts(); 
    IPC3bits.T3IP = 2; // Interrupt priority (must be in range [1..6]) 
    IEC0bits.T3IE = 1; // Enable timer T3 interrupts 

  while(1) { 
    putc(getc());
  } 

  return 0; 
} 

void _int_(12) isr_T3(void) { 
  char c[6]; 
  intToBinary(counter, c);
  putstr(c);
  putc('\n');
  counter++; 
  if(counter == 10) counter = 0;
  IFS0bits.T3IF = 0;
}

 