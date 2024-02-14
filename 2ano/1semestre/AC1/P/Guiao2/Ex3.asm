#Guiao 2 Ex3
	
	.data
str1: 	.asciiz "Uma string qualquer"
str2: 	.asciiz "AC1 – P"
	.eqv print_string,4 
 	.text
 	.globl main

main:	la $a0,str2 		# instrução virtual, decomposta pelo assembler em 2 instruções nativas
	ori $v0,$0,print_string # $v0 = 4
	syscall 		# print_string(str2);
	jr $ra 			# fim do programa 





#Alinhia B: 

#Endereço 	|Valor 	|Endereço 	|Valor
#0x10010014 	|0x41	|0x10010019	|0x20
#0x10010015	|0x43	|0x10010020	|0x50
#0x10010016	|0x31	|		|
#0x10010017	|0x20	|		|
#0x10010018	|0x13	|		|
