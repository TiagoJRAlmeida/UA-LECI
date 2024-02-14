#Guiao 4 Ex1
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
str: 	.space 21	#static char str(SIZE+1)
	.text
 	.globl main
 	
main: 	la $a0, str 		#read_string(str, SIZE)
 	li $a1, SIZE		#res = 0
	li $v0, read_string
	syscall 		
 	li $t0, 0		#num = 0
 	li $t1, 0		#i = 0
 	la $t2, str
 	
while:	addu $t3,$t2, $t1 	#str + i = &str[i]
 	lb $t4,0($t3) 		#str[i]
 	beq $t4,$0,ewhile 	#while( str[i]) != '\0') Salta quando str[i] = 0
 	blt $t4, '0', eif	#salta if de str[i] < '0' || str[i] > '9'
 	addi $t0, $t0, 1	#num++

eif:  	addi $t1, $t1, 1  	#i++
 	j while

ewhile:	move $a0, $t0		#print_int10(num)
	li $v0, print_int10
	syscall
	jr $ra			#fim do programa
