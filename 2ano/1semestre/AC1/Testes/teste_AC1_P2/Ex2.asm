# Teste P2 Ex2

# Mapa de registos
# val: $a0
# array: $a1
# fx: $t0
# k: $t1
# sum: $f0
# aux: $f2

	.data
zero:	.double 0.0
limit:	.double 0.035
	.text
	.globl main
	
# Função int calc(double val, double *array)

calc:	li $t0, 1 # fx = 1
	li $t1, 0 # k = 0
	la $t2, zero
	l.d $f0, 0($t2) # sum = 0.0
	la $t3, limit
	l.d $f6, 0($t3) # $f6 = 0.035 
	
do:	addi $t1, $t1, 1 # k + 1
	mul $t0, $t0, $t1 # fx = fx * (k + 1)
	mtc1 $t0, $f4 # $f4 = (double) fx
	l.d $f2, 0($a1) # aux = array[k]
	div.d $f2, $f2, $f4 # aux = array[k] / (double) fx
	add.d $f0, $f0, $f2 # sum = sum + aux
	s.d $f0, 0($a1) # array[k] = sum
	addi $t1, $t1, 1 # k++
	addi $a1, $a1, 8 # *array++
	
while:	ble $f2, $f6, ecalc
	j do
	
ecalc:	cvt.w.d $f0, $f0 
	mfc1 $t0, $f0
	move $v0, $t0
	jr $ra
	
	
	
	