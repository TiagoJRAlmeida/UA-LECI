# Guiao 9 Ex2

# Nota: Ao usar double as intruções acabam em ".d" e não em ".s" como em float
# (Fiquei 1 hora até descobrir que o problema neste código era que na linha 53 tinha "mov.s" invés de "mov.d"... -_-)
	
	
	# Função f2c
	.data
k1:	.double 5.0       # k1.1
    	.double 9.0       # k1.2
    	.double 32.0      # k1.3
	.text
f2c:	la $t0, k1
	l.d $f0, 0($t0) # la $t0, k1.1 (k1.1 = 5.0)
	l.d $f2, 8($t0) # la $t0, k1.2 (k1.2 = 9.0)
	l.d $f4, 16($t0) # la $t0, k1.3 (k1.3 = 32.0)
	sub.d $f12, $f12, $f4 # f12 = ft - 32.0
	div.d $f0, $f0, $f2 # $f0 = 5.0/9.0
	mul.d $f0, $f0, $f12 # $f0 = $f0 * $f12 = 5.0/9.0 * (ft - 32.0)
	jr $ra
	
	
	# Função main
	# int main(void){
	#	 double ft;
	#	 print_string("Introduza um valor em Fahreint: ");
	#	 ft = read_double();
	#	 print_string("O valor em centigrados é: ");
	#	 print_double(f2c(ft));
	# }
	.data
	.eqv print_double, 3
	.eqv print_char, 11
	.eqv print_str, 4
	.eqv read_double, 7
str1:	.asciiz "Introduza um valor em Fahreint: "
str2: 	.asciiz "O valor em centigrados é: "
	.text
	.globl main
main: 	addiu $sp, $sp, -4
	sw $ra, 0($sp)
	
	la $a0, str1
	li $v0, print_str # print_string("Introduza um valor em Fahreint: ");
	syscall
	li $v0, read_double # ft = read_double();
	syscall
	mov.d $f12, $f0 # $f12 = ft
	jal f2c # chamar a função f2c
	la $a0, str2 
	li $v0, print_str # print_string("O valor em centigrados é: ");
	syscall
	mov.d $f12, $f0
	li $v0, print_double # print_double(f2c(ft));
	syscall
	
	lw $ra, 0($sp)
	addiu $sp, $sp, 4
	li $v0, 0
	jr $ra
	
