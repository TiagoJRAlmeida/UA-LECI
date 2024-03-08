#include <detpic32.h>

// Contador tem 20Mhz de freq --> 50ns de periodo
// Periodo de 4.6hz: T = 1/4.6 = 0,217391304 seg
// Numero de contagens = 0,217391304 / 50 * 10⁻⁹ ~= 4347826  

void delay(){
    resetCoreTimer();
    while(readCoreTimer() < 4347826);
}

int main(void){

    // Configurar bits RE3 - RE6 como saidas
    TRISE = TRISE & 0xFF87;

    // Iniciar o counter
    unsigned int counter = 0;

    while(1){
        // Dar aos portos de saida (RE3 - RE6) o valor do counter
        LATE = (LATE & 0xFF87) | counter << 3;

        // delay (frequencia de 4.6hz)
        delay();

        // Incrementar o counter (mod 10)
        counter = (counter + 1) % 10;
    }

    return 0;
}
