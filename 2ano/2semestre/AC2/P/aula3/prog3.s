# Teoria do delay:
# O counter tem uma frequencia de 20Mhz, ou seja, em 1 segundo conta de 0 a 20.000.000.
# O periodo, ou seja o tempo de contar 1 vez, é 50ns (T = 1/2 * 10⁷= 5 * 10⁻⁸ = 50 * 10⁻⁹ = 50ns).
# Assim, para contar até 0,5 seg: 
# (5 * 10⁻¹)/(5 * 10⁻⁸) = 1 * 10⁷ = 10 000 000 ciclos 

# Outra forma de chegar ao mesmo resultado seria apenas pensar: 
# Se para contar até 20 milhoes demora 1 seg, em 0,5 segundos conta 10 milhões :P
        
        .data
        .equ ADDR_BASE_HI, 0xBF88
        .equ TRISB, 0x6040
        .equ PORTB, 0x6050
        .equ TRISE, 0x6100
        .equ LATE, 0x6120

        .equ RESET_CORE_TIMER, 12 
        .equ READ_CORE_TIMER, 11
        .text
        .globl main

main:   li $t0, ADDR_BASE_HI   

        # Inicializar os leds como OUTPUT
        lw  $t1,TRISE($t0) # 
        andi $t1,$t1,0xFFE1 # bits 4-1 as OUTPUT (1111 1111 1110 0001) 
        sw  $t1,TRISE($t0) # 

        # Iniciar os switchs como INPUT
        lw  $t1,TRISB($t0) #  
        ori $t1,$t1,0x000E # bits 3-1 as INPUT (0000 0000 0000 1110)  
        sw  $t1,TRISB($t0) # 

        li  $t2,0 # $t2 = counter

loop:   # Dar o valor do counter aos leds
        lw  $t1,LATE($t0) # 
        andi $t1,$t1,0xFFE1 # bits 4-1 ==> 0 (led off) 
        sll $t3,$t2,1 # Shift counter value to "position" 1 
        or  $t1,$t1,$t3 # Merge counter w/ LATE value 
        sw  $t1,LATE($t0) # 

        # Delay de 0,5 seg
        li $v0, RESET_CORE_TIMER
        syscall

delay:  li $v0, READ_CORE_TIMER
        syscall
        blt $v0, 10000000, delay
        
        addi $t2,$t2,1 

        j loop

        li $v0, 0
        jr $ra
