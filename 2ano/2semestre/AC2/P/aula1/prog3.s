# int main(void){
#     char c;
#     int cnt = 0;
#     do {
#         c = inkey();
#         if( c != 0 )
#             putChar( c );
#         else
#             putChar('.');
#         cnt++;
#     } while( c != '\n' );
#     printInt(cnt, 10);
#     return 0;
# }
###############################################
# Mapa de registos:
# $t0: cnt
# $t1: c

        .data
        .equ inkey, 1
        .equ getChar, 2
        .equ putChar, 3
        .equ printInt10, 7
        .text
        .globl main

main:   li $t0, 0

do:     li $v0, inkey
        syscall 
        move $t1, $v0

        beq $t1, 0, else
        move $a0, $t1
        li $v0, putChar
        syscall

        j while

else:   la $a0, '.' 
        li $v0, putChar
        syscall

while:  addi $t0, $t0, 1
        bne $t1, '\n', do

        move $a0, $t0
        li $v0, printInt10
        syscall

        li $v0, 0
        jr $ra

# NOTA: Apesar de o resultado da execução deste problema ser estranho, ao executar
#       o codigo C originalmente dado para traduzir, o resultado é o mesmo
#       logo deve estar certo, apenas um exercicio estranho, provavelmente para
#       além de experimentar o inkey() tambem observar a velocidade do clock.

