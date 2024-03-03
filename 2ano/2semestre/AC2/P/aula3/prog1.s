# RB0 vai ser um dos switch, por isso vai ser de entrada.
# RE0 vai ser um dos leds, por isso vai ser de saida

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

main:   lui   $t1,ADDR_BASE_HI # $t1=0xBF880000 

        # Alterar o RB0 para ser de entrada (TRISB(0) = 1)
        lw  $t2,TRISB($t1)  # READ  (Mem_addr = 0xBF880000 + 0x6040) 
        ori  $t2,$t2, 0x0001  # MODIFY (bit0=1 (1 means INPUT)) 
        sw  $t2,TRISB($t1)  # WRITE (Write TRISE register) 

        # Alterar o RE0 para ser de saida (TRISE(0) = 0)
        lw  $t3,TRISE($t1)  # READ  (Mem_addr = 0xBF880000 + 0x6100) 
        andi  $t3,$t3,0xFFFE  # MODIFY (bit0=0 (0 means OUTPUT)) 
        sw  $t3,TRISE($t1)  # WRITE (Write TRISE register) 

loop:   lw $t4, PORTB($t1)
        not $t4, $t4
        sw $t4, LATE($t1)
        j loop

        li $v0, 0
        jr $ra


