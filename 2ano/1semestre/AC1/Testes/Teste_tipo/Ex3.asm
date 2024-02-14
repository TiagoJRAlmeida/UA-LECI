#Ex3
# mapa de registos
# n_even : $t0
# n_odd : $t1
# p1 : $t2
# p2 : $t3
# listaA + SIZE : $t4
# *p1 : $t5
# temp : $t6
# *p2 : $t7
# listaB + n_odd : $t8


	.data
	.eqv SIZE, 10
listaA: .space 40
listaB: .space 40
	.eqv print_string, 4
	.eqv print_int10, 1
	.eqv read_int, 5
	.eqv print_char, 11
	.text
	.globl main
	
main:	li $t0, 0	# n_even = 0 
	li $t1, 0	# n_odd = 0
	
	la $t2, listaA	# p1 = a
	la $t3, listaB	# p2 = b
	
	addi $t4, $t4, SIZE 
	sll $t4, $t4, 2   # SIZE * 4
	add $t4, $t2, $t4 # $t4 = (a + N)
	
for:	
	bge $t2, $t4, for2 	# while(p1 < (a + N))
	li $v0, read_int
	syscall
	move $t5, $v0		# *p1 = read_int();
	sw $t5, 0($t2)
	addi $t2, $t2, 4	# p1++
	j for
	
	
for2: 	la $t2, listaA	# p1 = a
	la $t3, listaB	# p2 = b
	add $t2, $t2, $t6	# p1++
	bge $t2, $t4, for3  # while(p1 < (a + N))
	
if:	
	lw $t5, 0($t2)
	rem $t5, $t5, 2
	beq $t5, $0, else
	lw $t5, 0($t2)
	add $t3, $t3, $t6	# p2++
	sw $t5, 0($t3)
	addi $t6, $t6, 4
	addi $t1, $t1, 1	# n_odd++
	j for2
	
else:
	addi $t0, $t0, 1	# n_even++
	addi $t6, $t6, 4
	j for2
	
for3:
	la $t3, listaB	  # p2 = b
	add $t3, $t3, $t9	
	add $t8, $t8, $t1 # t8 = n_odd
	sll $t8, $t8, 2   # n_odd * 4
	add $t8, $t3, $t8 # $t8 = (b + n_odd)
	
	bge $t3, $t8, efor3
	lw $t6, 0($t3)
	move $a0, $t6
	li $v0, print_int10	# print_int10( * p2 );
	syscall	
	addi $t9, $t9, 4	
	j for3

efor3:
	li $v0, 0
	jr $ra

