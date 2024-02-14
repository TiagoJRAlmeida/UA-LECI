# Guiao 5 Ex1

#Mapa de registos:
# $t0 = i
# $t1 = lista ou &lista[0]
# $t2 = lista + i 
		
	.data
	.eqv SIZE, 5
	.eqv SIZEx4, 20

str: 	.asciiz "\nIntroduza um numero: "
 	
 	.align 2
lista:	.space SIZEx4 # SIZE * 4 
	
	.eqv print_string, 4
	.eqv read_int, 5
	.eqv print_char, 11
	.eqv print_int10, 1
	.eqv read_string, 8
	
	.text
	.globl main

main:	li $t0, 0		# i = 0                

for:	bge $t0, SIZE, efor	# não faz for se i >= SIZE
	la $a0, str		#print_string(str)
	li $v0, print_string
	syscall
	li $v0, read_int
	syscall			#						* = primeira iteração/ ** = segunda iteração
	la $t1, lista		# $t1 = lista            			*$t1 = 0x10010016/ **$t1 = 0x10010016
	sll $t2, $t0, 2		# i * 4						*$t2 = 0/ **$t2 = 4
	addu $t2, $t1, $t2	# $t2 = &lista[i] = lista + i * 4		*$t2 = 0 + $t1 =  0x10010016/ **$t2 = 4 + $t1 =  0x10010020
	sw $v0, 0($t2)		# $v0 tem o valor de retorno do read_int	*$valor do v0 guardado no endereço de $t2/ **valor do $v0 guardado no endereço de $t2
	addi $t0, $t0, 1 	#						*i = 1/ **i = 2
	j for
	
efor: 	li $v0, 0 
	jr $ra 		#fim do programa
	
	
#alinea c

#			|i ($t0) 	|lista ($t1) 	|&(lista[i])($t2) 	|($v0)
#-------------------------------------------------------------------------------------------
#Fim 1ª iteração	|1		|268501016	|268501016		|14
#Fim 2ª iteração	|2		|268501016	|268501020		|4660
#Fim 3ª iteração	|3		|268501016	|268501024		|11211350
#Fim 4ª iteração	|4		|268501016	|268501028		|-1
#Fim 5ª iteração	|5		|268501016	|268501032		|-1412589450


#Versão endereço hexadecimal

#			|i ($t0) 	|lista ($t1) 	|&(lista[i])($t2) 	|($v0)
#-------------------------------------------------------------------------------------------
#Fim 1ª iteração	|1		|0x10010018	|0x10010018		|14
#Fim 2ª iteração	|2		|0x10010018	|0x1001001C		|4660
#Fim 3ª iteração	|3		|0x10010018	|0x10010020		|11211350
#Fim 4ª iteração	|4		|0x10010018	|0x10010024		|-1
#Fim 5ª iteração	|5		|0x10010018	|0x10010028		|-1412589450


