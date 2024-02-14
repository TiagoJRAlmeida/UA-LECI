	.data
k1:	.double	0.0
k2:	.double	3.597
	.text
	.globl	prcells

# typedef struct{
# 		Align	Size	Offset
# char smp[10];	1 	10	0
# double av;	8 	8	10 -> 16
# int ns;	4 	4	24
# char id;	1 	1	28
# int sum;	4 	4	29 -> 32
# } t_cell;	8 	40

# Mapa de registos
# tc	: $a0
# size	: $a1
# res	: $f0
# aux	: $f2
# i	: $t0

prcells:
	la	$t1, k1
	l.d	$f0, 0($t1)		# res = 0.0
	li	$t0, 0			# i = 0

for:	bge	$t0, $a1, endfor	# for (i < size)

	mul	$t1, $t0, 36		# i * size
	addu	$t1, $a0, $t1		# &tc[i]

	addiu	$t2, $t1, 24		# &tc.ns
	lw	$t2, 0($t2)		# $t2 = tc.ns

	mtc1	$t2, $f4
	cvt.d.w	$f4, $f4		# $f4 = (double) tc[i].ns

	la	$t7, k2
	l.d	$f6, 0($t7)		# $f6 = 3.597
	div.d	$f2, $f4, $f6		# aux = (double)tc[i].ns / 3.597

	add.d	$f0, $f0, $f2		# res = res + aux

	s.d	$f2, 16($t1)		# tc[i].av = aux

	cvt.w.d	$f4, $f0		# $f4 = (int) res
	mfc1	$t2, $f4		# $t2 = $f4

	sw	$t2, 32($t1)		# tc[i].sum = (int)res

	addi	$t0, $t0, 1		# i++
	j	for

endfor:
	# res is already in $f0
	jr	$ra
