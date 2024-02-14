#Ex1
#Mapa de registos:
# val: $t0
# n: $t1
# min: $t2
# max: $t3

	.data
str1:	.asciiz "Digite ate 20 inteiros (Zero para terminar):"
str2:	.asciiz "Máximo/mínimo são: "
	.eqv print_string, 4
	.eqv print_int10, 1
	.eqv read_int, 5
	.eqv print_char, 11
	.text
	.globl main
	
main:	li $t1, 0
	li $t2, 0x7FFFFFFF
	li $t3, 0x80000000
	
	la $a0, str1
	li $v0, print_string
	syscall
	
do:	li $v0, read_int
	syscall
	li $t0, $v0
	
if:	beq $t0, $0, eif

if1:	ble $t0, $t3, if2
	li $t3, $t0
	
if2:	bge $t0, $t2, eif
	li $t2, $t0

eif:	addi $t1, $t1, 1

while:	blt $t1, 20, do
	bne $t0, 0, do
	
	la $a0, str2
	li $v0, print_string
	syscall
	la $a0, $t3
	li $v0, print_int10
	syscall
	la $a0, ':'
	li $v0, print_char
	syscall
	la $a0, $t4
	li $v0, print_int10
	syscall
	
	jr $ra