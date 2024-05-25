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

    TRISCbits.TRISC14 = 0;

    // Configure UART2: 115200, N, 8, 1  
    U2BRG = 10;
    U2MODEbits.BRGH = 0; // 0 = 16; 1 = 4;
    U2MODEbits.PDSEL = 0; // 0 = N; 1 = E; 2 = O;
    U2MODEbits.STSEL = 0;  // 0 = 1; 1 = 2;
    U2STAbits.UTXEN = 1;
    U2STAbits.URXEN = 1;
    U2MODEbits.ON = 1;

    // Configure UART2 interrupts, with RX interrupts enabled 
    // and TX interrupts disabled: 

    // enable U2RXIE, disable U2TXIE (register IEC1) 
    IEC1bits.U2TXIE = 0;
    IEC1bits.U2RXIE = 1;

    // set UART2 priority level (register IPC8)
    IPC8bits.U2IP = 2;

    // clear Interrupt Flag bit U2RXIF (register IFS1) 
    IFS1bits.U2RXIF = 0;

    // define RX interrupt mode (URXISEL bits) 
    U2STAbits.UTXISEL = 0;
    U2STAbits.URXISEL = 0; 

    // Enable global Interrupts 
    EnableInterrupts();

    while(1); 
    return 0; 
}

 
void _int_(32) isr_uart2(void){ 
    if (IFS1bits.U2RXIF == 1) { 
        // Read character from FIFO (U2RXREG) 
        // Send the character using putc() 
        char c = U2RXREG; 
        if(c == '?'){ putstr("AC2-Guiao 11"); }
        else{
            if(c == 'T'){ LATCbits.LATC14 = 1; }
            else if(c == 't'){ LATCbits.LATC14 = 0; }
            putc(c); 
        }

        // Clear UART2 Rx interrupt flag 
        IFS1bits.U2RXIF = 0;
    } 
}