#include <detpic32.h>

// Este exericio é no mesmo formato ao anterior, com a diferença que
// agora o contador (ainda mod 10) é decrescente e com uma frequencia de 2.7hz

// Calculo do numero de ciclos em uma frequencia de 2.7hz:
// O clock do MCU tem 20MHZ de freq e 50ns de periodo;
// 2.7hz --> T = 1/2.7 (seg)
// Numero de ciclos = T / 50 * 10⁻⁹ ~= 7407407

void delay(){
    resetCoreTimer();
    while(readCoreTimer() < 7407407);
}

int main(void){

    TRISE = TRISE & 0xFF87; // 1111 1111 1000 0111

    unsigned int counter = 0;

    while(1){
        LATE = (LATE & 0xFF87) | (counter << 3);

        delay();

        counter = (counter + 9) % 10;
    }

    return 0;
}
