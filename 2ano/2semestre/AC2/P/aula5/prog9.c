#include <detpic32.h>
#include "/home/tiago/github/UA-LECI/2ano/2semestre/AC2/P/Functions.c"

// Teoria:
// A frequencia de refrescamento é de 100hz, ou seja, em 1 segundo são contadas 100 vezes
// Ou seja, para o ctrl contar até 5 segundos, pode-se usar o refrescamento 500 vezes

int main(void){

    // declare variables 
    unsigned int counter, i;
    unsigned char value;
    unsigned int k = 50;
    unsigned int ctrl = 0;

    // configure RB8-RB14 as outputs
    TRISB = TRISB & 0x80FF; // (1000 0000 1111 1111)
    // configure RD5-RD6 as outputs
    TRISD = TRISD & 0xFF9F; // (1111 1111 1001 1111)
    // configure RE0 - RE5 as outputs
    TRISE = TRISE & 0xFFC0; // (1111 1111 1100 0000)
    // configure RB0 as input
    TRISB = TRISB | 0x0001; // (0000 0000 0000 0001)
    // configure RC14 as output
    TRISC = TRISC & 0xBFFF; // (1011 1111 1111 1111)

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

                //
                if(ctrl > 0){ ctrl--; }
                else{ LATCbits.LATC14 = 0; }

            } while(++i < k);
            
            if(PORTBbits.RB0 == 1 && counter > 0){ 
                counter--;
                k = 50;
            }
            else if(PORTBbits.RB0 == 1 && counter == 0){ 
                counter = 59;
                k = 50;
                ctrl = 500;
                LATCbits.LATC14 = 1;
            }
            else if(PORTBbits.RB0 == 0 && counter == 59){ 
                counter = 0;
                k = 20;
                ctrl = 500;
                LATCbits.LATC14 = 1;
            }
            else{ 
                counter++;
                k = 20;
            }
        } while(counter < 60);    
    } 
    return 0; 
}
