#Guiao 7 Ex1

# O argumento da função é passado em $a0
# O resultado é devolvido em $v0
# Sub-rotina terminal: não devem ser usados registos $sx


	.data
	.eqv print_int10, 1
	.text
strlen: li $t1,0 # len = 0;

while: 	lb $t0,0($a0) # *s               
 	addiu $a0,$a0,1 # s++
 	beq $t0,'\0',ewhile # salta se *s == 0 ==> while(*s++ != '\0')
 	addi $t1,$t1,1 # len++;
 	j while # 
 	
ewhile: move $v0, $t1
	jr $ra # o retorno é em $v0, logo já está carregado

	.data
str: 	.asciiz "Arquitetura de Computadores I"
	.text
	.globl main
	
main:
	addiu $sp, $sp, -4
	sw $ra,0($sp)
	
	la $a0, str
	jal strlen
	move $a0, $v1
	li $v0, print_int10
	syscall
	
	lw $ra, 0($sp)
	addiu $sp, $sp, 4
	li $v0, 0
	jr $ra
