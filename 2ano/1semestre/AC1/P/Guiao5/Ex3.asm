# Guiao 5 Ex3

#Código em C:

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#define SIZE 10
#define TRUE 1
#define FALSE 0

#void main(void){
#	static int lista[SIZE];
#	static char str1[]="\nIntroduza um numero: ";
#	static char str2[]="\nConteudo do array:\n";
#    	int houveTroca, i, aux, *p;
#
#    	// inserir aqui o código para leitura de valores e
#    	// preenchimento do array
#    	for(i = 0; i < SIZE; i++){
#    		print_string(str1);
# 		lista[i] = read_int();
#    	}
#
#    	do{
#        	houveTroca = FALSE;
#        	for (i=0; i < SIZE-1; i++){
#            		if (lista[i] > lista[i+1]){
#                		aux = lista[i];
#                		lista[i] = lista[i+1];
#                		lista[i+1] = aux;
#                		houveTroca = TRUE;
#            		}
#        	}
#    	} while (houveTroca==TRUE);
#
#    	// inserir aqui o código de impressão do conteúdo do array
#	print_string(str2); 
#    	for(p = lista; p < lista + SIZE; p++){
#    		print_int10( *p ); 
#		print_string("; "); 
#    	}
#}

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Mapa de registos
# $t1: *p
# $t2: lista + SIZEx4
# $t3: SIZE - 1
# $t4: houve_troca
# $t5: i
# $t6: lista
# $t7: lista + i

	.data
	.eqv FALSE,0
 	.eqv TRUE,1
 	.eqv SIZE, 10
 	.eqv SIZEminus1, 9
 	.eqv SIZEx4, 40
str1: 	.asciiz "\nIntroduza um numero: "
str2: 	.asciiz "\nConteudo do array:\n"
str3: 	.asciiz "; "
 	
 	.align 2
lista:	.space SIZEx4 

	.eqv print_string, 4
	.eqv read_int, 5
	.eqv print_char, 11
	.eqv print_int10, 1
	
 	.text
 	.globl main

main: 	li $t3, SIZEminus1		
	li $t5, 0 
	la $t6, lista						
 	addi $t2, $t6, SIZEx4


for:	bge $t5, SIZE, do			
	la $a0, str1				
	li $v0, print_string
	syscall
	li $v0, read_int
	syscall 
	sll $t7, $t5, 2									
	addu $t7, $t6, $t7					
	sw $v0, 0($t7)				
	addi $t5, $t5, 1			
	j for

do: 	li $t4,FALSE 				
	li $t5,0 
	
for2: 	bge $t5, $t3, while 	
			
if: 	sll $t7,$t5, 2 		
 	addu $t7,$t7,$t6 	
 	lw $t8,0($t7) 		
 	lw $t9,4($t7) 		
 	bge $t8,$t9,endif 	
 	sw $t8,4($t7) 		 			
 	sw $t9,0($t7) 					
 	li $t4, TRUE		
 	addi $t5, $t5, 1	
 	j for2			
 				
endif: 	addi $t5, $t5, 1 	
	j for2 		 	
 				
while:	beq $t4, TRUE, do	
	
	la $a0, str2		
	li $v0, print_string
	syscall
	li $t5, 0
	la $t6, lista
	
for3: 	bgeu $t6, $t2, efor3	#$t2 = endereço maximo; $t6 = primeiro endereço(antes dos ciclos)
	lw $t1, 0($t6)
	move $a0, $t1
	li $v0, print_int10
	syscall
	la $a0, str3
	li $v0, print_string
	syscall
	addiu $t6, $t6, 4
	j for3
	
efor3: 	li $v0, 0				
 	jr $ra 			
