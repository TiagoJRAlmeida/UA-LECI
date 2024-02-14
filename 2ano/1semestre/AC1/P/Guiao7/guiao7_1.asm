# O argumento da função é passado em $a0
# O resultado é devolvido em $v0
	.data
str1:	.asciiz "Arquitetura de Computadores I"
	.text
	.globl main	


strlen: 
	li 	$t1, 0           	# len = 0;

while: 
    	lb 	$t0, 0($a0)      	# Carrega o byte apontado por $a0 em $t0
    	beq 	$t0, $zero, endw 	# Verifica se *s == '\0'
    	addi 	$a0, $a0, 1    		# Avança para o próximo caractere na string
    	addi 	$t1, $t1, 1    		# len++
    	j 	while             	# Loop novamente

endw: 
    	move 	$v0, $t1       		# Retorna len em $v0
    	jr 	$ra              	# Retorna do subprograma
    
main:
	la 	$a0,str1
	jal	strlen
	move	$a0,$v0
	
	li	$v0,1
	syscall
	li	$v0,10
	syscall