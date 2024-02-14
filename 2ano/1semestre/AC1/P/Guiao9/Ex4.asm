# Guião 9 Ex4

# Mapa de registos de max:
# $t0/ $f2 = max
# $t1 = SIZE
# $t2/ $f4 = u
# $f6 = a[i]

	# Função max
	.data
	.text

max:	move $t0, $a0 # endereço inicial da array
	l.d $f2, 0($t0) # primeiro valor da array (a[0])
	move $t1, $a1 # tamanho da array
	addi $t1, $t1, -1 # n -= 1
	sll $t1, $t1, 3 # n *= 8
	addu $t2, $t1, $t0 # *u = p+n–1;
	addi $t0, $t0, 8 # *p++;
	
for_max:	
	bgt $t0, $t2, efor_max # for(; p <= u; p++){
	l.d $f6, 0($t0) # valor da array em loop (a[i])
	addi $t0, $t0, 8 # *p++;
	
	c.le.d $f6, $f2 # if(*p > max){ 
	bc1t for_max 
	mov.d $f2, $f6 # max = *p;
	j for_max # }
	
	
efor_max:	
	mov.d $f0, $f2 # $f0 = max
	jr $ra
	


	# Função main
	.data
a:	.space 80
	.eqv SIZE, 10
	.eqv read_double, 7
	.eqv print_double, 3
	.text
	.globl main 
	
main:	addiu $sp, $sp, -4
	sw $ra, 0($sp)
	li $t0, 0 # $t0 = i; i = 0

for:	bge $t0, SIZE, end_for # while(i < 10){
	li $v0, read_double # a[i] = read_double(); 
	syscall
	la $t1, a # $t1 recebe o endereço da array
	sll $t2, $t0, 3 # $t2 é o numero de bytes ocupados até agora ($t2 = i * 8) (x8 porque cada double ocupa 8 bytes) 
	addu $t1, $t1, $t2 # $t1 passa a ser o endereço do proximo double (endereço inicial da array + numero de bytes já ocupados)
	s.d $f0, 0($t1) # Guarda o valor lido no endereço $t1 (a[i] = read_double();)
	addi $t0, $t0, 1 # i++
	j for # }
	
end_for: 
	la $a0, a # $a0 recebe o endereço inicial da array
	li $a1, SIZE # $a1 recebe o tamanho da array
	jal max 
	mov.d $f12, $f0 # $f12 = $f0
	li $v0, print_double # print_double( max(a, SIZE) ); 
	syscall
	li $v0, 0
	lw $ra, 0($sp)
	addiu $sp, $sp, 4
	jr $ra