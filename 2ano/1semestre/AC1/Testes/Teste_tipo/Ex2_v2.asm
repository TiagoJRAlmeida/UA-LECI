#Ex2_v2
# mapa de registos
# i: $t0
# v: $t1
# &(val[0]) : $t2
# &(val[i]) : $t3
# &(val[SIZE/2]) : $t4
# &(val[i + SIZE/2]) : $t5
# i + SIZE/2 : $t6
# temp : $t7



	.data
str: 	.asciiz "Result is: "
val:	.word 8, 4, 15, -1987, 327, -9, 27, 16
	.eqv print_string, 4
	.eqv print_int10, 1
	.eqv read_int, 5
	.eqv print_char, 11
	.eqv SIZE, 8
	.text
	.globl main
	
main:
	li $t0, 0
	la $t2, val
	addi $t6, $t6, SIZE # t5= SIZE
	sll $t6, $t6, 2	# t6 = SIZE*4
	srl $t6, $t6, 1	# t6 = (SIZE*4)/2
	add $t4, $t2, $t6 # t4 = &val[SIZE*4/2]

do:
	add $t3, $t2, $t0 # $t3 = val[0] + i
	add $t5, $t4, $t0 # $t5 = val[SIZE*4/2] + i
	lw $t1, 0($t3)	# v = val[i]
	lw $t7, 0($t5)	# temp = val[i + SIZE*4/2]
	sw $t1, 0($t5)	# &val[i + SIZE*4/2] = val
	sw $t7, 0($t3)  # &val[i] = temp
	addi $t0, $t0, 4
	
while:
	addi $t7, $0, SIZE # temp= SIZE
	sll $t7, $t7, 2	# temp = SIZE*4
	srl $t7, $t7, 1	# temp = (SIZE*4)/2
	blt $t0, $t7, do

	la $a0, str
	li $v0, print_string #print_string(...);
	syscall
	li $t0, 0 # i = 0
	la $t3, val
	 	  	 
do2:
	lw $t7, 0($t3)
	move $a0, $t7
	li $v0, print_int10 # print_int10(val[i])
	syscall
	addi $t0, $t0, 4 # i++
	add $t3, $t2, $t0 # t3 = val[] + i
	  
	li $a0, ','
	li $v0, print_char # print_char(',')
	syscall
	
while2:
	addi $t7, $0, SIZE # temp= SIZE
	sll $t7, $t7, 2	# temp = SIZE*4
	blt $t0, $t7, do2
	
	li $v0, 0
	jr $ra
	
	
	