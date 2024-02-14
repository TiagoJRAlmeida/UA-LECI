
# struct cell {     | Size | Align |  Offset  |
#     char smp[10]; |   10 |     1 |  0 ->  0 |
#     double av;    |    8 |     8 | 10 -> 16 |
#     int ns;       |    4 |     4 | 24 -> 24 |
#     char id;      |    1 |     1 | 28 -> 28 |
#     int sum;      |    4 |     4 | 29 -> 32 |
# } t_cell;         |   40 |     8 |

		.data
double_zero: 	.double 0.0
k1: 		.double 3.597
		.text 
	
# Register map
# tc: $a0
# size: $a1
# res: $f0
# aux: $f4
# i: $t0

prcells:
    la $t1, double_zero
    l.d $f0, 0($t1) # res = 0.0;

    li $t0, 0 # i = 0;
for:
    bge $t0, $a1, endfor # while (i < size) {

    mul $t1, $t0, 40 # $t1 = i * 40
    addiu $t1, $a0, $t1 # $t1 += tc; ou seja, $t1 = endereço da struct + (i * 40)
    l.d $f6, 24($t1)
    cvt.d.w $f6, $f6 # $f6 = (double) tc[i].ns
    la $t2, k1
    l.d $f8, 0($t2) # $f8 = 3.597
    div.d $f4, $f6, $f8	# aux = (double) tc[i].ns / 3.597;
    add.d $f0, $f0, $f4	# res += aux;

    s.d $f4, 16($t1)# tc[i].av = aux;
    cvt.w.d $f6, $f0 # $f6 = (int) res
	
	
    mfc1 $t2, $f6 # $t2 = (int) res
    sw $t2, 32($t1)#     tc[i].sum = (int) res;
# ou sÃ³: s.s $f6, 32($t1)	# TRICKS!!!!

    addi $t0, $t0, 1#     ++i;
    j for # }
endfor:
    jr $ra # return res;
