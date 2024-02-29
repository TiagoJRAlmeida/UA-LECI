#void delay(unsigned int ms){
#    resetCoreTimer();
#    while(readCoreTimer() < K * ms);
#}
#########################################

# a) Um atraso de 1ms ou 0,001 seg é equivalente
#    á contagem de 20.000 ciclos do counter. Logo, se ms = 1, k = 20.000.

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

        move $a0, $t1
        jal delay

        addi $t0, $t0, 1

        j while 
        
        lw $ra, 0($sp)
	addiu $sp, $sp, 4
        
        jr $ra #


delay:  mul $a0, $a0, 20000
        
        li $v0, RESET_CORE_TIMER
        syscall

whileDelay:  
        li $v0, readCoreTimer
        syscall

        blt $v0, $a0, whileDelay

        li $v0, 0
        jr $ra


# Teoria:
# A frequencia do core timer é 20MGZ, ou seja, 50ns de periodo.
# O clock contar 20.000 vezes é equivalente a:
# 5 * 10⁻⁸ (seg) * 2 * 10⁴ = 10 * 10⁻⁴ (seg) = 10⁻³ (seg) = 0.001 seg.
# Ou seja, se $t1 for 1, o delay será 0.001seg ou 1ms, se for 10 vai ser:
# 5 * 10⁻⁸ (seg) * 2 * 10⁵ = 10 * 10⁻³ (seg) = 10⁻² (seg) = 0.01 seg.
# 0.01 seg = 10ms, ou seja a logica está correta, $t1 equivale ao tempo de delay em ms.

# $t1 | delay
#  1  |  1ms
#  10 |  10ms
# 100 |  100ms
# 1000|  1000ms = 1seg

# Testado com o cronometro e correto :))))