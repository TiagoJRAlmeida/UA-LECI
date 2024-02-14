#Ex3_v2
# mapa de registos
# n_even : $t0
# n_odd : $t1
# p1 : $t2
# p2 : $t3
# *p1 : $t4
# *p2 : $t5
# listaA + SIZE : $t6
# listaB + n_odd : $t7
# temp : $t8




	.data
	.eqv SIZE, 35
listaA: .space 140
listaB: .space 140
	.eqv print_string, 4
	.eqv print_int10, 1
	.eqv read_int, 5
	.eqv print_char, 11
	.text
	.globl main
	
main:	li $t0, 0		# n_even = 0 
	li $t1, 0		# n_odd = 0
	
	la $t2, listaA		# p1 = a
	la $t3, listaB		# p2 = b
	
	addi $t6, $t6, SIZE 
	sll $t6, $t6, 2   	# SIZE * 4
	add $t6, $t6, $t2 	# $t4 = (a + N)
	
for:	
	bge $t2, $t6, efor 	# while(p1 < (a + N))
	li $v0, read_int
	syscall
	move $t4, $v0		# *p1 = read_int();
	sw $t4, 0($t2)
	addi $t2, $t2, 4	# p1++
	j for
	
efor: 
	la $t2, listaA		# p1 = a
	la $t3, listaB		# p2 = b

for2: 
	bge $t2, $t6, efor2
	lw $t4, 0($t2)

if:
	rem $t8, $t4, 2	
	beq $t8, 0, else
	sw $t4, 0($t3)		# *p2 = *p1
	addi $t3, $t3, 4	# p2++
	addi $t1, $t1, 1	# n_odd++
	addi $t2, $t2, 4	# p1++
	j for2
	
else:
	addi $t0, $t0, 1	# n_even++
	addi $t2, $t2, 4 	# p1++
	j for2
	
efor2:
	la $t3, listaB		# p2 = b
	sll $t8, $t1, 2 	# n_odd * 4
	add $t7, $t3, $t8 	# $t7 = &listaB[0] + n_odd * 4
	
for3:
	bge $t3, $t7, efor3
	lw $t5, 0($t3)
	move $a0, $t5
	li $v0, print_int10
	syscall
	addi $t3, $t3, 4
	j for3	

efor3:
	li $v0, 0
	jr $ra
	
	