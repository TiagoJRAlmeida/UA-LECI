# Guiao 5 Ex2_v2

# Mapa de registos
# $t0: p
# $t1: *p (Registo temporário para guardar o valor armazenado em memória)
# $t2: lista + Size 

	.data
str1: 	.asciiz "\nConteudo do array:\n"
str2: 	.asciiz "; "
lista:	.word 8, -4, 3, 5, 124, -15, 87, 9, 27, 15	# a diretiva ".word" alinha num endereço múltiplo de 4
	.eqv print_int10,1
	.eqv print_string,4
	.eqv SIZE, 10
	.text
	.globl main

main: 	la $a0, str1 			# print_string("\nConteudo do array:\n")
	li $v0, print_string
	syscall
	la $t0, lista 			# p = lista
	li $t2, SIZE 			#
 	sll $t2, $t2, 2 		#  SIZE * 4
 	addu $t2, $t0, $t2 		# $t2 = lista + SIZE;

while: 	bgeu $t0, $t2, ewhile 		# while(p < lista+SIZE) {
 	lw $t1, 0($t0) 			# $t1 = *p;
 	move $a0, $t1
	li $v0, print_int10 		# print_int10( *p );
 	syscall 			
 	la $a0, str2 
 	li $v0, print_string		# print_string("; ");
	syscall
 	addiu $t0,$t0, 4 		# p++;
 	j while 			# }
 
ewhile: li $v0, 0
 	jr $ra 				# termina o programa 