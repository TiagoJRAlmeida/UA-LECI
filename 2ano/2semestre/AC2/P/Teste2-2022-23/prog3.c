#include <detpic32.h> 

volatile unsigned int counter = 15;

void putC(char byte){
    while(U2STAbits.UTXBF == 1);
    U2TXREG = byte; 
}

void putstr(char* str){
    while(*str != '\0'){
        putC(*str);
        str++;
    }
}

int main(void){
    
    // RE1-RE4 como OUTPUT
    TRISE = TRISE & 0xFFE1;
    
    LATE = (LATE & 0xFFE1) | counter << 1;

    // Configurar UART2: 9600,O,8,2
    U2BRG = 129;
    U2MODEbits.BRGH = 0;
    U2MODEbits.PDSEL = 2;
    U2MODEbits.STSEL = 1;
    U2STAbits.UTXEN = 1;
    U2STAbits.URXEN = 1;
    U2MODEbits.ON = 1;

    U2STAbits.URXISEL = 0;

    IEC1bits.U2RXIE = 1;
    IPC8bits.U2IP = 2;
    IFS1bits.U2RXIF = 0;

    EnableInterrupts();
    while(1);

    return 0;
}

void _int_(32) isr_UART2(void){
    char c = U2RXREG;
    if(c == 'U')
        counter = (counter + 1) % 16;
    else if(c == 'R'){ 
        counter = 0;
        putstr("RESET");
    }
    LATE = (LATE & 0xFFE1) | counter << 1;

    IFS1bits.U2RXIF = 0;
} 
