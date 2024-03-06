        .data
        .equ ADDR_BASE_HI, 0xBF88
        .equ TRISB, 0x6040
        .equ PORTB, 0x6050
        .equ TRISE, 0x6100
        .equ LATE, 0x6120
        .text
        .globl main

main:   li $t0, ADDR_BASE_HI   

        lw  $t1,TRISE($t0) # 
        andi $t1,$t1,0xFFE1 # bits 4-1 as OUTPUT (1111 1111 1110 0001) 
        sw  $t1,TRISE($t0) # 

        lw  $t1,TRISB($t0) #  
        ori $t1,$t1,0x000E # bits 3-1 as INPUT (0000 0000 0000 1110)  
        sw  $t1,TRISB($t0) # 

        li  $t2,0 # $t2 = counter

        lw  $t1,LATE($t0) # 
        andi $t1,$t1,0xFFE1 # bits 4-1 ==> 0 (led off) 
        sll $t3,$t2,1   # Shift counter value to "position" 1 
        or  $t1,$t1,$t3 # Merge counter w/ LATE value 
        sw  $t1,LATE($t0) # Update LATE register

        
