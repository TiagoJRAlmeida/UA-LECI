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

char* intToBinary(int value){
  switch(value){
    case 0:
      return "0000";
    case 1:
      return "0001";
    case 2:
      return "0010";
    case 3:
      return "0011";
    case 4:
      return "0100";
    case 5:
      return "0101";
    case 6:
      return "0110";
    case 7:
      return "0111";
    case 8:
      return "1000";
    case 9:
      return "1001";
    default:
      return "+++++";
  }
}
// Kprescaler = (Fpbclk)/((65535 + 1) * Fout) ==> Roof do valor obtido
// Com Fpbclk = 20 000 000 Hz e Fout = 5 Hz, temos:
// Kprescaler = roof de 61,04 = 62
// logo o prescaler será 64
// o novo PR3 = (20000000/64)/5 - 1 = 62499

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
    // Read character using getc() 
    // Send character using putc() 
    putc(getc());
  } 

  return 0; 
} 

void _int_(12) isr_T3(void) { 
  char* c = intToBinary(counter);
  putstr(c);
  putc('\n');
  counter++; 
  if(counter == 10) counter = 0;
  // Reset T3 interrupt flag 
  IFS0bits.T3IF = 0;
}

 