#Ex2
#Mapa de registos:
# i: $t0
# v: $t1
# &(val[0]): $t2

	.data
str1: 	.asciiz "Result is: "
lista:	.word 8, 4, 15, -1987, 327, -9, 27, 16
	.eqv SIZE, 8
	.eqv SIZEx4, 32
	.eqv print_string, 4
	.eqv print_int10, 1
	.eqv read_int, 5
	.eqv print_char, 11
	.text
	.globl main
	
main:	li $t0, 0

do: 	li $t2, lista
	sw $t1, $t0($t2)
	addi $t2, $t2, 16
	move $t2, $t1
	
while: 	addi $t0, $t0, 1
	blt $t0, 4, dp
	
	la $a0, str1
	li $v0, print_string
	syscall
	li $t0, 0
	li $t2, lista
	
do2:	sw $t1, $t0($t2)
	move $a0, $t1
	li $v0, print_int10
	syscall
	addi $t0, $t0, 4
	la $a0, ','
	li $v0, print_char
	syscall
	
while2:	blt $t0, SIZEx4, do2
	
	jr $ra