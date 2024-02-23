#void delay(unsigned int ms){
#    resetCoreTimer();
#    while(readCoreTimer() < K * ms);
#}
#########################################

# a) Como no exercicio anterior, um atraso de 1ms ou 0,01 seg é equivalente
#    á contagem de 200.000 ciclos do counter. Logo, se ms = 1, k = 200.000.

# b) ???

# Mapa de registo:
# $t0: counter
# $t1: ms

        .data
        .equ RESET_CORE_TIMER, 12
        .equ readCoreTimer, 11
        .equ readInt10, 5
        .equ PUT_CHAR, 3
        .equ PRINT_INT, 6
        .text
        .globl main

main:   addi $sp, $sp, -4
        sw $ra, 0($sp)

        li $t0, 0  # counter=0

        li $v0, readInt10
        syscall
        move $t1, $v0 

while:  la $a0, '\r'
        li $v0, PUT_CHAR
        syscall

        move $a0, $t0 
        li $a1, 0x0004000A
        li $v0, PRINT_INT
        syscall

        li $v0, RESET_CORE_TIMER
        syscall

        move $a0, $t1
        jal delay

        addi $t0, $t0, 1

        j while 
        
        lw $ra, 0($sp)
	    addiu $sp, $sp, 4
        
        jr $ra #


delay:  mul $a0, $a0, 200000

whileDelay:  
        li $v0, RESET_CORE_TIMER
        syscall

        li $v0, readCoreTimer
        syscall

        blt $v0, $a0, while

        li $v0, 0

        jr $ra
