# Teste P2 Ex1

# Mapa de registos
# argc:	$a0
# argv: $a1
# i: $t0
# p: $t1

	.data
	.eqv SIZE, 20
fla:	.space 80
str1:	.asciiz "Invalid argc"
	.eqv print_string, 4
	.eqv print_float, 2
	.text
	.globl main

# Função print

print:	addiu $sp, $sp, -12
	sw $ra, 0($sp)
	sw $s0, 4($sp)
	sw $s1, 8($sp)
	
	li $t0, 0 # i = 0
	la $t1, fla # *p = fla
	move $s0, $a0
	move $s1, $a1
	
if:	ble $s0, 1, else # while(argc > 1)
	bgt $s0, SIZE, else # while(argc <= SIZE)
	
for:	bge $t0, $s0, efor # while(i < argc)
	lb $a0, 0($s1) 
	li $a1, 10
	jal tof
	lb $v0, 0($t1)
	addi $t0, $t0, 1 # i++
	addi $t1, $t1, 1 # p++
	addi $s1, $s1, 1 # argv++
	j for
	
efor:	la $a0, fla
	move $a1, $s0
	jal aver
	mtc1 $v0, $f12 
	li $v0, print_float
	syscall
	j eprint
	
else:	la $a0, str1
	li $v0, print_string
	syscall
	
eprint:	lw $ra, 0($sp)
	lw $s0, 4($sp)
	lw $s1, 8($sp)
	addiu $sp, $sp, 12
	move $v0, $t1
	jr $ra	
