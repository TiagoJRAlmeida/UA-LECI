#Guiao 6 Ex1

#Mapa de registos:
# i: $t0


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
main:	li $t0, 0
	
for: 	bge $t0, SIZE, efor

	la $t1, array 		# $t1 = &array[0]
	sll $t2,$t0,2 		# i * 4 (cada ponteiro ocupa 4 bytes)
	addu $t2, $t2, $t1 	# $t2 = &array[i]
	lw $a0, 0($t2) 		# $a0 = array[i]
	li $v0, print_string
	syscall
	li $a0, '\n'
	li $v0, print_char
	syscall 
	
	addi $t0, $t0, 1
	j for

efor:	li $v0, 0
	jr $ra 
