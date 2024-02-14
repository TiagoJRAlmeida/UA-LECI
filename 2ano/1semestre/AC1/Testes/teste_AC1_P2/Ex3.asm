# Teste P2 Ex3

# typedef struct { 		Align	Size	Offset
# 	char id;		1	1	0
# 	double av;		8 	8	1
# 	int ns;			4	4	9
# 	char smp[18];		1	18	13
# 	int sum;		4	4	31 -> 32
# } t_sample;			8	40

# Mapa de registos
# ts  : $a0
# nval: $a1
# sum : $f0
# n   : $t1 
# k   : $t2
# acc : $t3
# pu  : $t4

	.data
zero:	.double 0.0
	.text
	.globl main
	
# Função float process(t_sample *ts, int nval)
	
process:
	la $t0, zero
	l.d $f0, 0($t0) # $f2 = 0.0; sum = 0.0;
	li $t3, 0 # acc = 0
	
	addu $t4, $a0, $a1
	
for:	bge $a0, $t4, efor
	lw $t5, 9($a0) # $t5 = ts->ns
	
for_2: 	bge $t2, $t5, efor2
	lw $t6, 13($a0) # $t6 = ts->smp
	la $t7, $t6
	addu $t7, $t7, $t2
	lb $t6, 0($t7)
	addu $t3, $t3, $t6
	j for_2

efor2:	sw $t3, 32($a0)
	mtc1 $t3, $f2
	cvt.d.w $f2, $f2 # (double) acc
	mtc1 $t5, $f4
	cvt.d.w $f4, $f4 # (double) ts->ns
	div.d $f6, $f2, $f4 # $f6 = (double) acc / (double) ts->ns
	s.d $f6, 1($a0)
	addu $f0, $f0, $f6
	j for
		
efor:	cvt.s.d $f0, $f0
	jr $ra