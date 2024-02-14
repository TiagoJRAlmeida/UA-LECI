#Guiao 4 Ex1_V2

# Mapa de registos
# num: $t0
# i: $t1
# str: $t2
# str+i: $t3
# str[i]: $t4

	.data
	.eqv SIZE,20
 	.eqv read_string,8 
 	.eqv print_int10,1
str: 	.space 21 
	.text
 	.globl main

main: 	la $a0, str 		# $a0=&str[0] (endere�o da posi��o
 				# 0 do array, i.e., endere�o
 				# inicial do array)
	li $a1, SIZE 		# $a1=SIZE
 	li $v0,read_string
 	syscall 		# read_string(str,SIZE)
 	li $t0, 0		# num=0;
 	li $t1, 0 		# i=0;

while: 				# while(str[i] != '\0')
 	la $t2, str 		# $t2 = str ou &str[0]
 	addu $t3, $t2, $t1 	# $t3 = str+i ou &str[i]
 	lb $t4,0($t3) 		# $t4 = str[i]
 	beq $t4,'\0',endw 	# {

if: 	blt $t4,'0',endif 	# if(str[i] >= '0' &&
 	bgt $t4,'9',endif 	# str[i] <= '9');
 	addi $t0,$t0, 1 	# num++;

endif:
 	addi $t1, $t1, 1 	# i++;
 	j while 		# }

endw: 	move $a0, $t0
	li $v0, print_int10  	# print_int10(num);
	syscall
 	jr $ra 			# termina o programa 
 	
 	
 	
 	
 	
#Endere�o de str ($t2)	|	Endere�o de str[i]($t3)	|	str[i]($t4)	|	i($t1)	|	num($t0)	|
#-----------------------------------------------------------------------------------------------------------------------|						
#			|				|			|	0	|	    0		| Val. iniciais		
#			|				|			|		|			| Fim 1� iter.
#			|				|			|		|			| Fim 2� iter.
# 			|				|			|		|			| Fim 3� iter.
#			|				|			|		|			| Fim 4� iter.
#			|				|			|		|			| Fim 5� iter.	
#			|				|			|		|			| Fim 6� iter.	
# 			|				|			|		|			| Fim 7� iter.	
#  			|				|			|		|			| Fim 8� iter.	