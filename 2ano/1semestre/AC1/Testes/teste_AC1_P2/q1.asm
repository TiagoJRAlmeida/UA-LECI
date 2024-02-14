# Register map
# array: $a0 -> $s0
# low: $a1 -> $s1
# high: $a2 -> $s2
# i: $s3
# npr: $s4
# p: $s5
primes:
    addiu $sp, $sp, -28
    sw $s5, 24($sp)
    sw $s4, 20($sp)
    sw $s3, 16($sp)
    sw $s2, 12($sp)
    sw $s1, 8($sp)
    sw $s0, 4($sp)
    sw $ra, 0($sp)

    move $s0, $a0
    move $s1, $a1
    move $s2, $a2

    move $s5, $s0        	# p = array;

    addi $s3, $s1, 1    	# i = low + 1;
    li $s4, 0        		# npr = 0;
for:
    bge $s3, $s2, endfor    # while (i < high) {

if:
    move $a0, $s3
    jal checkp
    bne $v0, 1, endif    	#     if (check(i) == 1) {

    sw $s3, 0($s0)        	#         *array = i;
    addiu $s0, $s0, 4    	#         ++array;
    addi $s4, $s4, 1    	#         ++npr;
endif:                		#     }

    addi $s3, $s3, 1    	#     ++i;
    j for            		# }
endfor:
    addu $t0, $s5, $s4
    sw $s4, 0($t0)        	# *(p + npr) = npr;

    move $v0, $s4


    lw $s5, 24($sp)
    lw $s4, 20($sp)
    lw $s3, 16($sp)
    lw $s2, 12($sp)
    lw $s1, 8($sp)
    lw $s0, 4($sp)
    lw $ra, 0($sp)
    addiu $sp, $sp, 28

    jr $ra            		# return npr;
