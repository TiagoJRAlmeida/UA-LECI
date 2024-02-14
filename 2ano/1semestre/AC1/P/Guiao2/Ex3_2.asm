#Guiao 2 Ex3_2

#Mapa de variaveis:
# $t0 = a;
# $t1 = b;
# $t2 = a + b;


	.data
str1: 	.asciiz "Introduza 2 numeros "
str2: 	.asciiz "A soma dos dois numeros e': "
	.eqv print_string,4 
	.eqv read_int,5
	.eqv print_int10,1
 	.text
 	.globl main

main:	la $a0,str1 		# instrução virtual, decomposta pelo assembler em 2 instruções nativas
	ori $v0,$0,print_string # $v0 = 4
	syscall 		# print_string(str1);
	ori $v0,$0,read_int
	syscall
	or $t0,$v0,$0 		# a($t0) = read_int();
	
	la $a0,str1 		# instrução virtual, decomposta pelo assembler em 2 instruções nativas
	ori $v0,$0,print_string # $v0 = 4
	syscall 		# print_string(str1);
	ori $v0,$0,read_int
	syscall
	or $t1,$v0,$0 		# b($t1) = read_int();
	
	la $a0,str2
	ori $v0,$0,print_string
	syscall			# print_string(str2);
	
	add $t2,$t1,$t0		# c = a + b;
	move $a0,$t2
	ori $v0,$0,print_int10	# print_int10(a + b);
	syscall
	
	jr $ra 			# fim do programa 