#int main(void) {
#    int counter = 0;
#    while(1) {
#        putChar('\r'); // cursor regressa ao inicio da linha no ecrã
#        printInt(counter, 10 | 4 << 16); // Ver nota de rodapé 1
#        resetCoreTimer();
#        while(readCoreTimer() < 200000);
#        counter++;  
#    }
#    return 0;
#}
############################################################################3


# a) A frequencia do core timer é 20MGZ, ou seja, 50ns de periodo.
#    O counter vai ser incrementado de 200.000 em 200.000 contações do core timer,
#    ou seja, de 0,01 seg em 0,01 seg. Isso, em frequencia é igual a:
#    f = 1/0,01 = 1/1*10⁻² = 1000 hz = 1khz

# b)

        .data
        .equ READ_CORE_TIMER,11
        .equ RESET_CORE_TIMER,12
        .equ PUT_CHAR, 3
        .equ PRINT_INT, 6
        .text
        .globl main
        

main:   li $t0, 0  # counter=0

while:  la $a0, '\r'
        li $v0, PUT_CHAR
        syscall

        move $a0, $t0 
        li $a1, 0x0004000A
        li $v0, PRINT_INT
        syscall

        li $v0, RESET_CORE_TIMER
        syscall

while2: li $v0, READ_CORE_TIMER
        syscall
        blt $v0, 200000, while2

        addi $t0, $t0, 1

        j while 

        jr $ra #
