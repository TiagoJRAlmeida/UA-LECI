# Este exercicio é igual ao prog1, com a diferença que estamos a 
# usar Inputs diferentes.
# RD8 vai ser INT1, por isso vai ser de entrada (é o botão de pulse).
# RE0 vai ser um dos leds, por isso vai ser de saida

# NOTAS:
# 1- Em OR, 0 é o elemento neutro e 1 é o elemento absorvente;
# 2- Em ADD, 1 é o elemento neutro e 0 é o elemento absorvente;
# 3- Caso queiramos definir uma porta como INPUT, usamos o OR porque o 1 é absorvente;
# 4- Caso queiramos definir uma porta como OUTPUT, usamos o ADD porque o 0 é absorvente; 
# 5- TRIS serve para ler ou escrever o valor de um porto para que seja ou INPUT(1) ou OUTPUT(0);
# 6- PORT serve para ler o valor atual de um INPUT;
# 7- LAT server para escrever um valor de um OUTPUT;
# 8- Em XOR, um dos elementos ser 1, inverte o valor do outro, porque se o outro for 0, o resultado 
#    é 1, e se for 1 o resultado é 0. (XOR 1, 0 = 1)(XOR 1, 1 = 0);   


# Teoria do shift de 8 bits feito ao RE0:
# RE tem 8 bits: RE0, RE1, RE2, ..., RE7;
# Queremos tranferir o valor de RE0 para RE7
# 0000 0001 --> (SLL 1) 0000 0010
# 0000 0001 --> (SLL 2) 0000 0100
# 0000 0001 --> (SLL 3) 0000 1000
# 0000 0001 --> (SLL 4) 0001 0000
# 0000 0001 --> (SLL 5) 0010 0000
# 0000 0001 --> (SLL 6) 0100 0000
# 0000 0001 --> (SLL 7) 1000 0000
# Conclusão: seria usado um SLL 7;
 

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

        # Alterar o RD8 para ser de entrada (TRISD(8) = 1)
        lw  $t1,TRISD($t0)  # READ  (Mem_addr = 0xBF880000 + 0x6040) 
        ori  $t1,$t1,0x0100  # MODIFY (bit8=1 (1 means INPUT)) 0000 0001 0000 0000 
        sw  $t1,TRISD($t0)  # WRITE (Write TRISE register) 

        # Alterar o RE0 para ser de saida (TRISE(0) = 0)
        lw  $t1,TRISE($t0)  # READ  (Mem_addr = 0xBF880000 + 0x6100) 
        andi  $t1,$t3,0xFFFE  # MODIFY (bit0=0 (0 means OUTPUT)) 1111 1111 1111 1110 
        sw  $t1,TRISE($t0)  # WRITE (Write TRISE register) 

loop:   lw $t1, PORTD($t0) # Ler o valor da entrada RDx
        andi $t1, $t1, 0x0100 # Por todos os valors de RDx a 0 menos RD8 (0000 0001 0000 0000)

        lw $t2, LATE($t0) # Ler o valor da saida REx (o led)
        andi $t2, $t2, 0xFFFE # Pôr apenas o valor da saida RE0 = 0 (o led fica desligado)(1111 1111 1111 1110)
        #####################################################
        srl $t1, $t1, 8 # DUVIDA: Em teoria, devia ser sll, e não srl, mas na prática isto estava a funcionar. WHY?!?!?!
        #####################################################
        xori $t2, $t2, 0xFFFF # Inverte o resultado (Led ligado = 0; Led desligado = 1). É basicamente um NOT. Ver notas em caso de duvida.
        or $t2, $t2, $t1 # Junta os valores da entrada RDx com a saida REx. Assim, se um deles for ligado 
        sw $t2, LATE($t0) 

        j loop

        li $v0, 0
        jr $ra
