#Ex1_corrigido
#Mapa de registos:
# val: $t0
# n: $t1
# min: $t2
# max: $t3

#Erros do Ex1:
# Mau uso do la, li e move;
# Não meter o print_string dentro do "do" loop
# erro ao terminar o while( tinha de usar 2 whiles)
# no final ao dar print ao min, usei um $t4 inves de $t2 (distração)


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
	
do:	la $a0, str1
	li $v0, print_string
	syscall
	li $v0, read_int
	syscall
	move $t0, $v0
	
if:	beq $t0, $0, eif

if1:	ble $t0, $t3, if2
	move $t3, $t0
	
if2:	bge $t0, $t2, eif
	move $t2, $t0

eif:	addi $t1, $t1, 1

while:	bne $t0, 0, while2
	j ewhile
	
while2:	blt $t1, 20, do
	j ewhile
	
ewhile:	la $a0, str2
	li $v0, print_string
	syscall
	move $a0, $t3
	li $v0, print_int10
	syscall
	li $a0, ':'
	li $v0, print_char
	syscall
	move $a0, $t2
	li $v0, print_int10
	syscall
	
	li $v0, 0
	jr $ra
