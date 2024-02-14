# Guião 9 Ex1

# Mapa de registos:
# $t0/$f0 = val 
# $t1/$f2 = 2.59375
# $f2/$f12 = res (%f12 quando for para dar print)
# $f4 = 0.0 

	.data
	.eqv read_int, 5
	.eqv print_float, 2
	.eqv print_string, 4
k1: 	.float 2.59375
k2:	.float 0.0
space:  .asciiz "\n"
	.text
	.globl main
	
main:

do:	li $v0, read_int
	syscall
	move $t0, $v0 # $t0 = val
	la $t1, k1 # $t1 = 2.59375
	l.s $f2, 0($t1) # $f2 = 2.59375
	mtc1 $t0, $f0 # $f0 = (float) val
	cvt.s.w $f0, $f0 # mover $f0 para coproc 1
	mul.s $f2, $f0, $f2 # Multiplicar $f2 = $f0 * $f2 = (float)val * 2.59375 = res
	mov.s $f12, $f2 # Mover $f2 para $f12 ($f12 = res) ($f12 é o valor a ser printado)
	li $v0, print_float
	syscall
	la $a0, space
	li $v0, print_string
	syscall
	la $t1, k2 # $t1 = 0.0
	l.s $f4, 0($t1) # $f4 = 0.0
	c.eq.s $f4, $f2 # if($f4 = $f2) <=> if(res = 0.0)
	bc1t fim # se a condiçao anterior for verdadeira, vai para o "fim"
	j do # se a condiçao anterior for falsa, vai para o "do"
	
fim:	li $v0, 0
	jr $ra
