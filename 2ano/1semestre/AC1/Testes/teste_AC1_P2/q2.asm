    	.data
double_zero: .double 0.0
	.text
	
# Register map
# array: $a0
# thd: $f12
# val: $f14
# n: $a1
# i: $t0
# aux: $f4
# sum: $f6

proc:
    	la $t1, double_zero
    	l.d $f6, 0($t1)	# sum = 0.0;

    	li $t0, 0 # $t0 = i = 0;
for:
    	bge $t0, $a1, endfor #	while (i < n) {
	
	sll $t1, $t0, 3	# $t1 = i * 8
    	addu $t1, $a0, $t1 # $t1 = *array + $t1
    	l.d $f8, 0($t1) # $f8 = array[i]
    	add.d $f4, $f8, $f14 #	aux = array[i] + val;

if:
    	c.lt.d $f12, $f4
    	bc1f else # if (aux > thd) {

    	s.d $f12, 0($t1) # array[i] = thd;
    	add.d $f6, $f6, $f12  # sum += thd;

    	j endif # }
else: #	else {
    	s.d $f4, 0($t1) # array[i] = aux;
    	add.d $f6, $f6, $f4 # sum += aux;
endif: # }
	addi $t0, $t0, 1 # i++;
	j for #     
endfor: # }
    	mtc1 $a1, $f8
    	cvt.d.w $f8, $f8 # (double) n
	div.d $f0, $f6, $f8 # sum / (double) n
	jr $ra # return sum / (double) n;
