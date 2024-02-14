#Guiao 7 Ex3

# Mapa de registos:
# $a0 = src
# $a1 = dst
# $t0 = i
# $t1 = src[i]

	# Função strcpy
	.data
	.text
strcpy: li $t0, 0 # i = 0
	lb $t1, 0($a0)
	
do:	sb $t1, $t0($a1)
	
	addi $t0, $t0, 1
	lb $t1, $t0($a0)
	beq $t1, '\0', edo
	j do
	
edo:    move $v0, $a1
	jr $ra
	
	
	# Função Main
	.data
	.text
	.globl main
	
main:	
	