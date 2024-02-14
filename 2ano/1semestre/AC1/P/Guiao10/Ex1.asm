	.data #linha 10 do prof
um: 	.float 1.0

	#float xtoi(float x, int y)
	.text
	#mapa de registos:
	# $?0: i
	# $t1: abs(y)
	# $?1: y
	# $f0: result
	# f12 : x	linha 20 do prof
xtoy:	addiu $sp, $sp, -20
	sw $ra, 0($sp)
	sw $?0, 4($sp)	# i
	sw $?1, 8($sp)	# y
	s.s $f20, 12($sp)	# float x
	s.s $f22, 16($sp)	# result
	mov.s $f20, $f12 	# guardar x
	li $?0, 0	# i = 0
	la $t3, um
	l.s $f22, 0($t3)	# result = 1.0
	move $?1, $a0 		# perservar y para futuro uso
	jal abs			# abs(y) - note-se que $a0 contém y por isso pode-se manter para entra...
	move $t1, $v0		# convém mudar o output de aba para outro registo porque $v0 é usado pa...
for_xt: bge $
