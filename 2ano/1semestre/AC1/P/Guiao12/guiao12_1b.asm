	.data
str1:	.asciiz "\nMedia: "
	.align 2
st_array:	.space 176	# student st_array[MAX_STUDENTS]
	.align 2		# opcional
media:	.space 4		# float media
	.text
	.globl main
main:	
	la	$a0,st_array
	li	$a1,3
	jal 	read_data
	jr	$ra
# Mapa de Registos:
# st:	$a0 --> $t0
# ns:	$a1 --> $t1
# i:	$t2
read_data:
	move	$t0,$a0
	move	$t1,$a1
	li	$t2,0		# i = 0
for:	
	bge	$t2,$t1,endf	# while ( i < ns ) {
	li	$v0,5 
	syscall
	mul	$t3,$t2,44
	addu	$t3,$t0,$t3	# $t3 = &st[i] = &(st[i].idnumber)
	sw	$v0,0($t3)	# st[i].id = read_int()
	
	addiu	$a0,$t3,4	# $a0 = &st[i].first_name
	li	$a1,17
	li	$v0,8
	syscall			# read_str(st[i].first_name,17)
	
	addiu	$a0,$t3,22	# $a0 = &st[i].last_name
	li	$a1,14
	li	$v0,8
	syscall			# read_str(st[i].last_name,17)
	
	li	$v0,6
	syscall
	s.s	$f0,40($t3)	# st[i].grade = read_float()
	addi	$t2,$t2,1	# i++
	j for			# }
endf:
	jr	$ra