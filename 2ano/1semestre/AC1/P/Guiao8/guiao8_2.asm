# Mapa de Registos
# n:		$a0 -> $s0
# b:		$a1 -> $s1
# s:		$a2 -> $s2
# p:		$s3
# digit:	$t0
# Sub-rotina intermédia
	
	.data
	.text
	.globl main
	
itoa:
	addiu	$sp,$sp,-16
	sw	$ra,0($sp)
	sw	$s0,4($sp)
	sw	$s1,8($sp)
	sw	$s2,12($sp)
	sw	$s3,16($sp)
	move	$s0,$a0
	move	$s1,$a1
	move	$s2,$a2
	move	$s3,$a2
while:
	div	$s0,$s1
	mfhi	$t0
	div	$s0,$s1
	mflo	$s1
	jal	toascii
	# inserir *p++ = toascii( digit );
	addi	$s3,$s3,1
	bge	$a0,0,endw
	j 	while
endw:
	sb	$0,0($s3)
	jal	strrev
	lw	$ra,0($sp)
	lw	$s0,4($sp)
	lw	$s1,8($sp)
	lw	$s2,12($sp)
	lw	$s3,16($sp)
	addiu	$sp,$sp,16
	jr	$ra