# Guiao 11 Ex1_v2
	
	.data 
	.eqv print_string, 4
	.eqv print_ui10, 36
	.eqv print_char, 11
	.eqv print_float, 2
	.eqv of_id, 0
	.eqv of_fn, 4
	.eqv of_ln, 22
	.eqv of_gr, 40
	.align 2
stg:	.word 72343		#unsigned int id_number;
	.asciiz "Napoleao"	#char first_name[18];
	.space 9		
	.asciiz "Boinaparte"	#char last_name[15];
	.space 4
	.align 2		#.space 3
	.float 5.1		# float grade;
	
str1:	.asciiz "\nN. Mec: "
str2:	.asciiz "\nNome: "
str3:	.asciiz "\nNotas: "

	.text
	.globl main
main:	la $a0, str1
	li $v0, print_string
	syscall
	la $t0, stg
	lw $a0, of_id($t0)	#stg.id_number
	li $v0, print_ui10
	syscall
	la $a0, str2
	li $v0, print_string
	syscall
	la $a0, stg
	addiu $a0, $a0, of_ln	# end.inicial da struct (stg) + 
	li $v0, print_string
	syscall
	li $a0, ','
	li $v0, print_char
	syscall
	la $a0, stg
	addiu $a0, $a0, of_fn
	li $v0, print_string
	syscall
	la $t0, stg
	l.s $f12, of_gr($t0)
	li $v0, print_float
	syscall 
	li $v0, 0
	jr $ra
	
