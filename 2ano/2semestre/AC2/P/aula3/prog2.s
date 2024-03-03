# Este exercicio é igual ao prog1, com a diferença que estamos a 
# usar Inputs diferentes.
# RD8 vai ser um dos switch, por isso vai ser de entrada.
# RE0 vai ser um dos leds, por isso vai ser de saida

        .data
        .equ ADDR_BASE_HI,0xBF88 # Base address: 16 MSbits
        
        .equ TRISB,0x6040    # TRISB address is 0xBF886040 
        .equ PORTB, 0x6050 # PORTB address is 0xBF886050
        .equ LATB, 0x6060 # LATB address is 0xBF886060
        
        .equ TRISE,0x6100    # TRISE address is 0xBF886100
        .equ PORTE,0x6110    # PORTE address is 0xBF886110 
        .equ LATE,0x6120   # LATE  address is 0xBF886120 
        
        .equ TRISD, 0x60C0 # TRISD address is 0xBF8860C0
        .equ PORTD, 0x60D0 # PORTD address is 0xBF8860D0
        .text
        .globl main

main:   lui   $t0,ADDR_BASE_HI # $t1=0xBF880000 

        # Alterar o RB0 para ser de entrada (TRISB(0) = 1)
        lw  $t1,TRISD($t0)  # READ  (Mem_addr = 0xBF880000 + 0x6040) 
        ori  $t1,$t1,0x0100  # MODIFY (bit0=1 (1 means INPUT)) 0000 0001 0000 0000 
        sw  $t1,TRISD($t0)  # WRITE (Write TRISE register) 

        # Alterar o RE0 para ser de saida (TRISE(0) = 0)
        lw  $t1,TRISE($t0)  # READ  (Mem_addr = 0xBF880000 + 0x6100) 
        andi  $t1,$t3,0xFFFE  # MODIFY (bit0=0 (0 means OUTPUT)) 
        sw  $t1,TRISE($t0)  # WRITE (Write TRISE register) 

loop:   lw $t1, PORTD($t0) 
        andi $t1, $t1, 0x0100

        lw $t2, LATE($t0)
        andi $t2, $t2, 0xFFFE
        srl $t1, $t1, 8
        xori $t2, $t2, 
        or $t2, $t2, $t1
        sw $t2, LATE($t0) 

        j loop

        li $v0, 0
        jr $ra
