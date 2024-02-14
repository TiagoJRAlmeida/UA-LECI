#Guiao 6 Ex2

#Mapa de registos:
# $t0: p 
# $t2: pultimo

	.data
	.eqv SIZE, 3
	.eqv print_string, 4
	.eqv print_char, 11

str1:	.asciiz "Array"
str2: 	.asciiz "de"
str3: 	.asciiz "ponteiros"

array:	.word str1, str2, str3

	.text
	.globl main
	
main:
	la $t0,array 		# $t0 = p = &array[0] = array
	li $t2,SIZE 		# $t0 = 3
	sll $t2,$t2,2 		# $t0 = 3 * 4 = 12
	addu $t2,$t2,$t0 	# $t2 = pultimo = array + SIZE
	
for:  	bgeu $t0, $t2, efor	# p >= penultimo salta para o fim do for
	lw $a0, 0($t0)		# $a0 = *p
	li $v0, print_string
	syscall
	li $a0, '\n'
	li $v0, print_char
	syscall
	
	addi $t0,$t0, 4		# p++
	j for
	
efor:
	jr $ra