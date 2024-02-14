# Guiao 5 Ex2

# Mapa de registos
# $t0: p
# $t1: *p (Registo temporário para guardar o valor armazenado em memória)
# $t2: lista + Size 

	.data
	.eqv SIZE, 10
lista:	.word 8, -4, 3, 5, 124, -15, 87, 9, 27, 15
str:	.asciiz "\nConteudo da array:\n"
pve: 	.asciiz "; "
	.eqv print_string, 4
	.eqv read_int, 5
	.eqv print_char, 11
	.eqv print_int10, 1
	.eqv read_string, 8
	.text
	.globl main
	
main:	la $a0, str
	li $v0, print_string
	syscall
	la $t0, lista		# p = lista
	li $t2, SIZE
	sll $t2, $t2, 2		# tem de ser SIZE * 4 por serem inteiros
	addu $t2, $t2, $t0	#lista + SIZE (ultimo endereço)
	
for: 	bgeu $t0, $t2, efor
	lw $a0, 0($t0)		# *p
	li $v0, print_int10 	# print_int10(*p)
	syscall	
	la $a0, pve
	li $v0, print_string
	syscall
	addiu $t0, $t0, 4	# p++:
	j for
	
efor: 	li $v0, 0
	jr $ra
	
