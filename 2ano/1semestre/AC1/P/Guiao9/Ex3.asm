# Guião 9 Ex3

	
	# Função average
	.data
	.text 
	
average: 
	move $t0, $a1 # $t0 = 10; $t0 = i;
	addi $t0, $t0, -1 # $t0 = 9
	mtc1 $0, $f2 # $f2 = 0
	cvt.d.w $f2, $f2 # converte word para double. Neste caso 0 para 0.0 ($f2 = 0.0) ($f2 = sum)
	
for_av:	blt $t0, $0, endfor_av # while(i >= 0){
	move $t1, $t0 # $t1 = i 
	sll $t1, $t1, 3 # $t1 *= 8 
	move $t2, $a0 # $t2 = endereço inicial da array
	addu $t2, $t2, $t1 # $t2 é o endereço do valor em loop no momento ($t2 += $t1) ($t1 = i * 8)
	l.d $f4, 0($t2) # $f4 = a[i]
	add.d $f2, $f2, $f4 # $f2 += a[i] (sum += a[i])
	addi $t0, $t0, -1 # i--
	j for_av # }
	
endfor_av: 
	mtc1 $a1, $f4 # $f4 = SIZE = 10
	cvt.d.w $f4, $f4 # converter 10 (word) para double => $f4 = 10.0
	div.d $f0, $f2, $f4 # $f0 = sum / SIZE
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
	jal average 
	mov.d $f12, $f0 # $f12 = $f0
	li $v0, print_double # print_double( average(a, SIZE) ); 
	syscall
	li $v0, 0
	lw $ra, 0($sp)
	addiu $sp, $sp, 4
	jr $ra
