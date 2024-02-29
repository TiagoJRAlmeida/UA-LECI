#include <detpic32.h>

// É o mesmo que o prog3, com a diferença que é possivel controlar a 
// frequencia com os botões 'A' e 'N'.

// A tecla 'A' ao ser precionada, irá dobrar a frequencia.
// A tecla 'N' retorna a frequencia ao normal. 

// Teoria:
// Ao dobrar a frequencia, i.e. para 2hz, 10hz, 20hz, o que vai acontecer é que,
// invés de periodo do ser respetivamente: 1seg, 0.2seg e 0.1seg 
// será respetivamente: 0.5seg, 0.1seg, 0.05seg.
// Logo, uma maneira de resolver este código seria dividir o delay, sempre que a tecla 'A' 
// é premida.
// C.A.: T: 1/2 = 0.5 seg; T=1/10 = 0.1seg; T=1/20=0.05seg

// Funciona :D

void delay(unsigned int ms){
    resetCoreTimer();
    while(readCoreTimer() < 20000 * ms);
}

int main(void){
    int cnt1 = 0;
    int cnt5 = 0;
    int cnt10 = 0;
    int normalDelay = 100;
    int delayValue = 100;
    int key;

    while(1){
        key = inkey();
        if(key == 97 || key == 65){
            delayValue /= 2;
        }
        else if(key == 78 || key == 110){
            delayValue = normalDelay;
        }
        else{
            delay(delayValue);
            cnt10++;
            if(cnt10 >= 10 && cnt10 % 10 == 0){ cnt1++; }
            if(cnt10 >= 2 && cnt10 % 2 == 0) {cnt5++;}
            
            printInt(cnt1, 10 | 4 << 16);
            putChar('\t');
            printInt(cnt5, 10 | 4 << 16);
            putChar('\t');
            printInt(cnt10, 10 | 4 << 16);
            putChar('\r');
        }
    }

    return 0;
}