#Ex2_corrigido
#Mapa de registos:
# i: $t0
# v: $t1
# &lista[0]: $t2
# &lista[i]: $t3
# i+SIZEx4/2: $t4
# &lista[0] + $t4 : $t5
# aux : $t6
# &lista[i + SIZE/2] : $t7


#Erros do Ex2:
# Mau uso do la, li e move;
# ambos os do, while estavam mal feitos

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
	
main:	li $t0, 0		# i = 0
	la $t2, lista		# $t2 = &lista[0]
	li $t4, SIZEx4		# $t4 = SIZEx4
	srl $t4, $t4, 1		# $t4 = $t4 / 2
	add $t5, $t2, $t4	# $t5 = &lista[0] + $t4

do:	add $t3, $t2, $t0	# $t3 = &lista[0] + i = &lista[i]
	lw $t1, 0($t3)		# $t1 = lista[i] 				# v = val[i]
	add $t4, $t4, $t0	# $t4 = $t4 + i
	add $t7, $t5, $t0	# $t7 = &lista[i + SIZE/2]
	lw $t6, 0($t7)		# $t6 = lista[i + SIZE/2]			# aux = val[i+size/2]
	sw $t1, 0($t7)								# val[i + SIZE/2] = v
	sw $t6, 0($t3)								# val[i] = aux

	
while: 	addi $t0, $t0, 4	# i = i + 4 
	blt $t0, 16, do
	
	la $a0, str1
	li $v0, print_string
	syscall
	la $t3, lista
	li $t0, 0
	
do2:	lw $t1, 0($t3)
	move $a0, $t1
	li $v0, print_int10
	syscall
	li $a0, ','
	li $v0, print_char
	syscall
	addi $t3, $t3, 4
	addi $t0, $t0, 4
	
	
while2:	blt $t0, SIZEx4, do2
	
	li $v0, 0
	jr $ra
