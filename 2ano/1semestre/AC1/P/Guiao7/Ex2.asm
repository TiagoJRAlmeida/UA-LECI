#Guiao 7 Ex2

# Mapa de registos:
# str: $a0 -> $s0 (argumento � passado em $a0)
# p1: $s1 (registo callee-saved)
# p2: $s2 (registo callee-saved)
# aux: $t0

	# Fun��o exchange
	.data
	.text
exchange: 
	addiu $sp, $sp, -4
	sw $t0, 0($sp)
	sb $t0, 0($a0) # aux = *c1; 
	sb $a1, 0($a0) # *c1 = *c2;
	sb $a0, 0($t0) # *c2 = aux;
	lw $t0, 0($sp)
	addiu $sp, $sp, 4
	jr $ra
	
	# Fun��o strrev
	.data
	.text
strrev: addiu $sp,$sp,-16 # reserva espa�o na stack
 	sw $ra,0($sp) # guarda endere�o de retorno
 	sw $s0,4($sp) # guarda valor dos registos
 	sw $s1,8($sp) # $s0, $s1 e $s2
 	sw $s2,12($sp) #
	move $s0,$a0 # registo "callee-saved"
 	move $s1,$a0 # p1 = str
 	move $s2,$a0 # p2 = str

while1: lb $t0,0($s2) # *p2 
	beq $t0, '\0', while2 # while( *p2 != '\0' ) {
 	addi $s2, $s2, 1 # p2++;
 	j  while1 # }
 	addi $s2, $s2, -1 # p2--;

while2: bge $s1, $s2, ewhile # while(p1 < p2) {
 	move $a0, $s1 #
 	move $a1, $s2 #
 	jal exchange # exchange(p1,p2)
 	addi $s1, $s1, 1 # p1++;
 	addi $s2, $s2, -1 # p2--;
 	j while2 # }
 	
ewhile: move $v0,$s0 # return str
 	lw $ra,0($sp) # rep�e endere�o de retorno
 	lw $s0,4($sp) # rep�e o valor dos registos
 	lw $s1,8($sp) # $s0, $s1 e $s2
 	lw $s2,12($sp) #
 	addiu $sp,$sp,16 # liberta espa�o da stack
 	jr $ra # termina a sub-rotina 
 	
 	# Fun��o main
	.data
str:	.asciiz "ITED - orievA ed edadisrevinU"
	.eqv print_string, 4
	.text
	.globl main
	
main:	addiu $sp, $sp, -4
	sw $ra,0($sp)
	la $s0, str
	move $a0, $s0
	jal strrev
	move $s0, $v0
	move $a0, $s0
	li $v0, print_string
	syscall
	
	lw $ra, 0($sp)
	addiu $sp, $sp, 4
	li $v0, 0
	jr $ra
