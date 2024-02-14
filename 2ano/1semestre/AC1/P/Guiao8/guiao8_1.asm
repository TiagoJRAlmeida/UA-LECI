# Mapa de Registos
# res:		$v0
# s:		$a0
# *s:		$t0
# digit:	$t1
	
	
# Falta fazer c)

	.data
str:	.asciiz "2020 e 2024 sao anos bissextos"
	.text
	.globl main
atoi:
	li	$v0,0
	li	$t1,0
while:	
	lb	$t0,0($a0)
	bltu	$t0,0x30,endw
	bgtu	$t0,0x39,endw
	addiu	$t1,$t0,-0x30
	addiu	$a0,$a0,1
	mulu	$v0,$v0,10
	addu	$v0,$v0,$t1
	j	while
endw:
	jr 	$ra
	
main:
	la	$a0,str
	jal	atoi
	move	$a0,$v0
	li	$v0,1
	syscall
	li	$v0,10
	syscall
		
		