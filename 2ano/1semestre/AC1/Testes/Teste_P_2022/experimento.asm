	.data
X1:	.asciiz "TEST1"
	.align 2
X2:	.space 20
X3:
	.text
	.globl main

main:	la $t4,X2		# $t4 = 0x10010008
	ori $t5, $0, 4		# $t5 = 4
	xor $t0, $t0, $t0	# $t0 = 0
	xor $t1, $t1, $t1	# $t1 = 0

L1:	beq $t0, $t5, L2	# while($t0 != $t5) 
	add $t2, $t0, $t0	# $t2 = $t0 + $t0			*$t2 = 0		**$t2 = 2		***$t2 = 4		****$t2 = 6
	add $t3, $t2, $t2	# $t3 = $t2 + $t2			*$t3 = 0		**$t3 = 4		***$t3 = 8		****$t3 = 12
	addu $t3, $t3, $t4	# $t3 = $t3 + $t4			*$t3 = 0x10010008	**$t3 = 0x1001000C	***$t3 = 0x10010010	****$t3 = 0x10010014
	sw $t2, 0($t3)		# endereço $t3 tem o valor $t2		*0x10010008 = 0		**0x1001000C = 2	***0x10010010 = 4	****0x10010014 = 6
	add $t1, $t1, $t2	# $t1 = $t1 + $t2			*$t1 = 0		**$t1 = 2		***$t1 = 6		****$t1 = 12
	addi $t0, $t0, 1	# $t0++         			*$t0 = 1		**$t0 = 2		***$t0 = 3		****$t0 = 4
	j L1

L2:	sw $t1, 4($t3)		#0x10010018 = 12
	jr $ra	
	