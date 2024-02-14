#Guiao 4 Ex2
# Mapa de registos
# num: $t0
# &str[0] : $t1
# str[0] : $t2


	.eqv read_string,8
	.eqv print_int10,1
	.eqv SIZE, 20
	.eqv SIZEmais1 , 21
	.data

str:	.space SIZEmais1	# static cahr str[SIZE + 1]
	.text
	.globl main
	
main: 	li $t0, 0	#num = 0
	la $a0, str	#read_string(str, SIZE)
	li $a1, SIZE
	li $v0, read_string
	syscall
	la $t1, str
	
while: 	lb $t2, 0($t1)
	beq $t2, $0, ewhile
	blt $t2, '0', eif
	bgt $t2, '9', eif
	addi $t0, $t0, 1
	
eif: 	addiu $t1, $t1, 1
	j while
	
ewhile:	move $a0, $t0
	li $v0, print_int10
	syscall
	jr $ra
	
