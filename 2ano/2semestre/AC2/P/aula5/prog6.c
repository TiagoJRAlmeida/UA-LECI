#include <detpic32.h>
#include "/home/tiago/github/UA-LECI/2ano/2semestre/AC2/P/Functions.c"

int main(void){

    // declare variables 
    unsigned int counter, i;
    unsigned char value;

    // configure RB8-RB14 as outputs
    TRISB = TRISB & 0x80FF; // (1000 0000 1111 1111)
    // configure RD5-RD6 as outputs
    TRISD = TRISD & 0xFF9F; // (1111 1111 1001 1111)
    // configure RE0 - RE5 as outputs
    TRISE = TRISE & 0xFFC0; // (1111 1111 1100 0000)

    while(1){
        counter = 0;
        do{ 
            i = 0;
            // Alterar os valores dos leds
            LATE = (LATE & 0x0000) | counter; 

            do{ 
                // Alterar o valor dos display
                value = toBcd(counter); 
                send2displays(value); 
                delay(10);

            } while(++i < 50); 
            counter++;
        }while(counter < 60);    
    } 
    return 0; 
}
