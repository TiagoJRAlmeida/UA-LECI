#include <detpic32.h>
#include "/home/tiago/github/UA-LECI/2ano/2semestre/AC2/P/Functions.c"

int main(void){

    // declare variables 
    unsigned int counter, i;

    // configure RB8-RB14 as outputs
    TRISB = TRISB & 0x80FF; // (1000 0000 1111 1111)
    // configure RD5-RD6 as outputs
    TRISD = TRISD & 0xFF9F; // (1111 1111 1001 1111)

    counter = 0;

    while(1){ 
        i = 0; 
        do{ 
            send2displays(counter); 
            // wait 20 ms (1/50Hz)
            delay(20);


        } while(++i < 10); 
        // increment counter (mod 256)
        counter++; 
    } 
    return 0; 
}
