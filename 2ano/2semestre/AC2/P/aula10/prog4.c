#include <detpic32.h>

// <****** EX5 da part1 *******> 

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

// versão 600,N,8,1
// int main(void) { 
//   // Taxa de transmissão/receção pretendida
//   U2BRG = ((20000000 + 8*600)/(16*600)) - 1; 
//   U2MODEbits.BRGH = 0; // Baudrate speed; 0 = 16; 1 = 4; 
//   U2MODEbits.PDSEL = 0;  // Tipo de paridade; 0 = N; 1 = E; 2 = O; 3 = N;
//   U2MODEbits.STSEL = 0; // Número de stop bits; 0 = 1; 1 = 2; 
//   U2STAbits.UTXEN = 1; // Ativar o modulo de transmissão
//   U2STAbits.URXEN = 1; // Ativar o modulo de receção
//   U2MODEbits.ON = 1; // Ativar a UART

//   while(1){ 
//     putstr("String de teste\n");
//     delay(1000);
//   } 

//   return 0;
// }

//#############################################################################

// versão 1200,O,8,2
// int main(void) { 
//   // Taxa de transmissão/receção pretendida
//   U2BRG = ((20000000 + 8*1200)/(16*1200)) - 1; 
//   U2MODEbits.BRGH = 0; // Baudrate speed; 0 = 16; 1 = 4; 
//   U2MODEbits.PDSEL = 2;  // Tipo de paridade; 0 = N; 1 = E; 2 = O; 3 = N;
//   U2MODEbits.STSEL = 1; // Número de stop bits; 0 = 1; 1 = 2; 
//   U2STAbits.UTXEN = 1; // Ativar o modulo de transmissão
//   U2STAbits.URXEN = 1; // Ativar o modulo de receção
//   U2MODEbits.ON = 1; // Ativar a UART

//   while(1){ 
//     putstr("String de teste\n");
//     delay(1000);
//   } 

//   return 0;
// }

//#############################################################################

// versão 9600,E,8,1
// int main(void) { 
//   // Taxa de transmissão/receção pretendida
//   U2BRG = ((20000000 + 8*9600)/(16*9600)) - 1; 
//   U2MODEbits.BRGH = 0; // Baudrate speed; 0 = 16; 1 = 4; 
//   U2MODEbits.PDSEL = 1;  // Tipo de paridade; 0 = N; 1 = E; 2 = O; 3 = N;
//   U2MODEbits.STSEL = 0; // Número de stop bits; 0 = 1; 1 = 2; 
//   U2STAbits.UTXEN = 1; // Ativar o modulo de transmissão
//   U2STAbits.URXEN = 1; // Ativar o modulo de receção
//   U2MODEbits.ON = 1; // Ativar a UART

//   while(1){ 
//     putstr("String de teste\n");
//     delay(1000);
//   } 

//   return 0;
// }

//#############################################################################

// versão 19200,N,8,2; 
// int main(void) { 
//   // Taxa de transmissão/receção pretendida
//   U2BRG = ((20000000 + 8*19200)/(16*19200)) - 1; 
//   U2MODEbits.BRGH = 0; // Baudrate speed; 0 = 16; 1 = 4; 
//   U2MODEbits.PDSEL = 0;  // Tipo de paridade; 0 = N; 1 = E; 2 = O; 3 = N;
//   U2MODEbits.STSEL = 1; // Número de stop bits; 0 = 1; 1 = 2; 
//   U2STAbits.UTXEN = 1; // Ativar o modulo de transmissão
//   U2STAbits.URXEN = 1; // Ativar o modulo de receção
//   U2MODEbits.ON = 1; // Ativar a UART

//   while(1){ 
//     putstr("String de teste\n");
//     delay(1000);
//   } 

//   return 0;
// }

//#############################################################################

// versão 115200,E,8,1; 
// int main(void) { 
//   // Taxa de transmissão/receção pretendida
//   U2BRG = ((20000000 + 8*115200)/(16*115200)) - 1; 
//   U2MODEbits.BRGH = 0; // Baudrate speed; 0 = 16; 1 = 4; 
//   U2MODEbits.PDSEL = 1;  // Tipo de paridade; 0 = N; 1 = E; 2 = O; 3 = N;
//   U2MODEbits.STSEL = 0; // Número de stop bits; 0 = 1; 1 = 2; 
//   U2STAbits.UTXEN = 1; // Ativar o modulo de transmissão
//   U2STAbits.URXEN = 1; // Ativar o modulo de receção
//   U2MODEbits.ON = 1; // Ativar a UART

//   while(1){ 
//     putstr("String de teste\n");
//     delay(1000);
//   } 

//   return 0;
// }

//#############################################################################

// versão 230400,E,8,2; 
// int main(void) { 
//   // Taxa de transmissão/receção pretendida
//   U2BRG = ((20000000 + 2*230400)/(4*230400)) - 1; 
//   U2MODEbits.BRGH = 1; // Baudrate speed; 0 = 16; 1 = 4; 
//   U2MODEbits.PDSEL = 1;  // Tipo de paridade; 0 = N; 1 = E; 2 = O; 3 = N;
//   U2MODEbits.STSEL = 1; // Número de stop bits; 0 = 1; 1 = 2; 
//   U2STAbits.UTXEN = 1; // Ativar o modulo de transmissão
//   U2STAbits.URXEN = 1; // Ativar o modulo de receção
//   U2MODEbits.ON = 1; // Ativar a UART

//   while(1){ 
//     putstr("String de teste\n");
//     delay(1000);
//   } 

//   return 0;
// }

//#############################################################################

// versão 460800,O,8,1; 
// int main(void) { 
//   // Taxa de transmissão/receção pretendida
//   U2BRG = ((20000000 + 2*460800)/(4*460800)) - 1; 
//   U2MODEbits.BRGH = 1; // Baudrate speed; 0 = 16; 1 = 4; 
//   U2MODEbits.PDSEL = 2;  // Tipo de paridade; 0 = N; 1 = E; 2 = O; 3 = N;
//   U2MODEbits.STSEL = 0; // Número de stop bits; 0 = 1; 1 = 2; 
//   U2STAbits.UTXEN = 1; // Ativar o modulo de transmissão
//   U2STAbits.URXEN = 1; // Ativar o modulo de receção
//   U2MODEbits.ON = 1; // Ativar a UART

//   while(1){ 
//     putstr("String de teste\n");
//     delay(1000);
//   } 

//   return 0;
// }

//#############################################################################

// versão 576000,N,8,1; 
int main(void) { 
  // Taxa de transmissão/receção pretendida
  U2BRG = ((20000000 + 2*576000)/(4*576000)) - 1; 
  U2MODEbits.BRGH = 1; // Baudrate speed; 0 = 16; 1 = 4; 
  U2MODEbits.PDSEL = 0;  // Tipo de paridade; 0 = N; 1 = E; 2 = O; 3 = N;
  U2MODEbits.STSEL = 0; // Número de stop bits; 0 = 1; 1 = 2; 
  U2STAbits.UTXEN = 1; // Ativar o modulo de transmissão
  U2STAbits.URXEN = 1; // Ativar o modulo de receção
  U2MODEbits.ON = 1; // Ativar a UART

  while(1){ 
    putstr("String de teste\n");
    delay(1000);
  } 

  return 0;
}


