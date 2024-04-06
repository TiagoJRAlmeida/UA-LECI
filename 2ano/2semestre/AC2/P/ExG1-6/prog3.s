        .data
        .equ ADDR_BASE_HI,0xBF88 # Base address: 16 MSbits
        .equ TRISB,0x6040    # TRISB address is 0xBF886040 
        .equ PORTB, 0x6050 # PORTB address is 0xBF886050
        .equ LATB, 0x6060 # LATB address is 0xBF886060
        .equ TRISE,0x6100    # TRISE address is 0xBF886100
        .equ PORTE,0x6110    # PORTE address is 0xBF886110 
        .equ LATE,0x6120   # LATE  address is 0xBF886120 
        .text
        .globl main

main:   lui $t0, ADDR_BASE_HI

        lw $t1, TRISB($t0)
        andi $t1, $t1, 0
        ori $t1, $t1, 0x000F
        sw $t1, TRISB($t0)

        lw $t1, TRISE($t0)
        ori $t1, $t1, 1
        andi $t1, $t1, 0xFF00
        sw $t1, TRISE($t0)

while:  lw $t1, PORTB($t0)
        li $t3, 0x0000
        li $t2, 0x000F

        andi $t2, $t1, 0x0008 
        srl $t2, $t2, 3
        or $t3, $t3, $t2 

        andi $t2, $t1, 0x0004 
        srl $t2, $t2, 1
        or $t3, $t3, $t2 
        
        andi $t2, $t1, 0x0002 
        sll $t2, $t2, 1
        or $t3, $t3, $t2 
        
        andi $t2, $t1, 0x0001 
        sll $t2, $t2, 3
        or $t3, $t3, $t2 

        sll $t3, $t3, 4

        andi $t2, $t1, 0x000F
        or $t3, $t3, $t2

        sw $t3, LATE($t0)

        j while

        li $v0, 0
        jr $ra   
