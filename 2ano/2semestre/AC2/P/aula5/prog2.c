#include <detpic32.h>
#include prog1.c

void delay(unsigned int ms){
    resetCoreTimer();
    while(readCoreTimer() < (20000 * ms));
}

int main(void) { 

    // configure RB8-RB14 as outputs
    TRISB = TRISB & 0x80FF; // (1000 0000 1111 1111)

    // configure RD5-RD6 as outputs
    TRISD = TRISD & 0xFF9F; // (1111 1111 1001 1111)

    while(1) { 
        send2displays(0x15); 
        
        // wait 0.2s
        delay(200); 
    } 

    return 0;
}
