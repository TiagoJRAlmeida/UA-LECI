#Guiao 3 Ex1

# Mapa de registos:

# soma: $t0
# value: $t1
# i: $t2

  
      .data
strl: .asciiz "Introduza um numero: "
str2: .asciiz "Valor ignorado\n"
str3: .asciiz "A soma dos positivos e': "
      .eqv print_string,4
      .eqv read_int, 5
      .eqv print_int10, 1
      .text
      .globl main
 	
main: li $t2,0 # i = 0
      li $t0,0 # soma = 0

for: 	bge $t2, 5, endfor # se i>= 5 ou while(i < 5)
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
	la $a0, strl 		# print_string("Introduza um numero: ")
	li $v0, print_string	#
	syscall
	li $v0, read_int   	# value = read_int();
	syscall
	move $t1, $v0
	
	ble $t1, $0, else 	# se value <= 0 vai para o else, ou simplesmente if(value > 0);
	add $t0, $t0, $t1 	# soma += value;
	j endif
	
else: 	la $a0, str2		# print_string("Valor ignorado\n");
	li $v0, print_string	#
	syscall
	
endif: #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
	addi $t2, $t2, 1	# i++;
	j for
	
endfor: la $a0, str3		# print_string("A soma dos positivos e': ");
	li $v0, print_string 	#
	syscall
	move $a0, $t0
	li $v0, print_int10	# print_int10(soma); 
	syscall
	jr $ra
	
	
