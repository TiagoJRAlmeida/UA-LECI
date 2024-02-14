#Guiao 8 Ex1

# res = $v0
# s: $a0
# *s: $t0
# digit: $t1
# aux: $t2

	.eqv print_int10, 1
	.text
atoi:	li $v0, 0 	#res = 0
while:	lb $t0,0($a0)	# le *s
	blt $t0, '0', ewhile	
	bgt $t0, '9', ewhile
	li $t2, '0'
	sub $t1,$t0, $t2 #digit = *s - '0'
	addiu $a0, $a0, 1 #s++
	mul $v0, $v0, 10 #res = 10 * res
	addu $v0, $v0, $t1 #res = res + digit
	j while

ewhile: jr $ra # $v0 já tem res 

	.data
str:	.asciiz "2020 e 2024 sao anos bissextos"
	.text
	.globl main
	
main: 	addiu $sp, $sp, -4
	sw $ra, 0($sp)
	
	la $a0, str
	jal atoi
	move $a0, $v0
	li $v0, print_int10
	syscall
	
	lw $ra, 0($sp)
	addiu $sp, $sp, 4
	li $v0, 0
	jr $ra