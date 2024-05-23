#include <detpic32.h>
#include "/home/tiago/github/UA-LECI/2ano/2semestre/AC2/P/Functions.c"

// Integre no programa anterior o sistema de visualização. Faça as alterações que permitam a 
// visualização do valor da amplitude da tensão nos displays de 7 segmentos, em decimal. O 
// programa  deverá:  i)  efetuar  5  sequências  de  conversão  A/D  por  segundo  (frequência  de 
// amostragem  de  5  Hz),  cada  uma  delas  com  8  amostras;  ii)  enviar  informação  para  o 
// sistema de visualização a cada 10 ms (frequência de refrescamento de 100 Hz). Utilize, na 
// organização do seu código, o programa-esqueleto que se apresenta de seguida: 

// Nota: 
// A palavra-chave volatile dá a indicação ao compilador que a variável pode ser alterada de 
// forma  não  explicitada  na  zona  de  código  onde  está  a  ser  usada  (i.e.,  noutra  zona  de  código, 
// como  por  exemplo  numa  rotina  de  serviço  à  interrupção).  Com  esta  palavra-chave  força-se  o 
// compilador  a,  sempre  que  o  valor  da  variável  seja  necessário,  fazer  o  acesso  à  posição  de 
// memória  onde  essa  variável  reside,  em  vez  de usar  uma  eventual  cópia,  potencialmente com 
// um valor desatualizado, residente num registo interno do CPU. 
 


volatile unsigned char voltage = 0; // Global variable  

int main(void) { 
    unsigned int cnt = 0; 
    unsigned int x = 4;
    unsigned int N = 8;

    // Ligar o OUTPUT do enable dos displays
    TRISD = TRISD & 0xFF9F; // (1111 1111 1001 1111) 

    // Ligar o OUTPUT dos displays (RB8 - RB14)
    TRISB = TRISB & 0x80FF; // (1000 0000 1111 1111)
    
    // Configure all (digital I/O, analog input, A/D module) 
    TRISBbits.TRISB4 = 1; // RB4 digital output disconnected 
    AD1PCFGbits.PCFG4= 0; // RB4 configured as analog input 
    AD1CON1bits.SSRC = 7; // Conversion trigger selection bits: in this mode an internal counter ends sampling and starts conversion 
    AD1CON1bits.CLRASAM = 1;  // Stop conversions when the 1st A/D converter interrupt is generated. At the same time, hardware clears the ASAM bit 
    AD1CON3bits.SAMC = 16;    // Sample time is 16 TAD (TAD = 100 ns) 
    AD1CON2bits.SMPI = N-1; // Interrupt is generated after N samples (replace N by the desired number of consecutive samples) 
    AD1CHSbits.CH0SA = x;   // replace x by the desired input analog channel (0 to 15) 
    AD1CON1bits.ON = 1; 

    // Configure interrupt system 
    IPC6bits.AD1IP = 2;  // configure priority of A/D interrupts 
    IFS1bits.AD1IF = 0;  // clear A/D interrupt flag 
    IEC1bits.AD1IE = 1;  // enable A/D interrupts 

    EnableInterrupts();  // Global Interrupt Enable 
    while(1){ 
        if(cnt == 0) {  // 0, 200 ms, 400 ms, ... (5 samples/second) 
         
            // Start A/D conversion 
            AD1CON1bits.ASAM = 1;
        } 
        // Send "voltage" value to displays 
        send2displays(voltage);

        cnt = (cnt + 1) % 20; 
        // Wait 10 ms
        delay(10); 
    } 
    return 0; 
}  


void _int_(27) isr_adc(void) { 
    // Read 8 samples (ADC1BUF0, ..., ADC1BUF7) and calculate average 
    int i;
    int sum = 0;
    int average = 0;
    int *p = (int*)(&ADC1BUF0);
    for(i = 0; i < 16; i++){
        sum += p[i*4];
        printInt10(p[i*4]);
        putChar(' ');
    }

    putChar('\r');
    average = sum/8;
    // Calculate voltage amplitude 
    average = (33*average + 511)/1023;
    // Convert voltage amplitude to decimal and store the result in the global variable "voltage"  
    voltage = toBcd(average);
    // Reset AD1IF flag 
    IFS1bits.AD1IF = 0; 
}
