
# int main(void) { 
#     int value; 
#     while(1) { 
#         printStr("\nIntroduza um inteiro (sinal e módulo): "); 
#         value = readInt10(); 
#         printStr("\nValor em base 10 (signed): "); 
#         printInt10(value); 
#         printStr("\nValor em base 2: "); 
#         printInt(value, 2); 
#         printStr("\nValor em base 16: "); 
#         printInt(value, 16); 
#         printStr("\nValor em base 10 (unsigned): "); 
#         printInt(value, 10); 
#         printStr("\nValor em base 10 (unsigned), formatado: "); 
#         printInt(value, 10 | 5 << 16); // ver nota de rodapé 3 
#     } 
#     return 0; 
# }
#######################################################################

# Mapa de registos:
# value: $t0
#


        .data
        .equ readInt10, 5
        .equ printInt, 6
        .equ printInt10, 7
        .equ printStr, 8
msg1:   .asciiz "\nIntroduza um inteiro (sinal e módulo): "
msg2:   .asciiz "\nValor em base 10 (signed): "
msg3:   .asciiz "\nValor em base 2: "
msg4:   .asciiz "\nValor em base 16: "
msg5:   .asciiz "\nValor em base 10 (unsigned): "
msg6:   .asciiz "\nValor em base 10 (unsigned), formatado: "
        .text
        .globl main

main:   # printStr("\nIntroduza um inteiro (sinal e módulo): ");
        la $a0, msg1
        li $v0, printStr
        syscall 
        # value = readInt10(); 
        li $v0, readInt10
        syscall 
        move $t0, $v0 

        # printStr("\nValor em base 10 (signed): "); 
        la $a0, msg2
        li $v0, printStr
        syscall 
        # printInt10(value);
        move $a0, $t0
        li $v0, printInt10
        syscall

        # printStr("\nValor em base 2: "); 
        la $a0, msg3
        li $v0, printStr
        syscall 
        # printInt(value, 2);
        move $a0, $t0
        li $a1, 2
        li $v0, printInt
        syscall 

        # printStr("\nValor em base 16: "); 
        la $a0, msg4
        li $v0, printStr
        syscall 
        # printInt(value, 16); 
        move $a0, $t0
        li $a1, 16
        li $v0, printInt
        syscall 

        # printStr("\nValor em base 10 (unsigned): "); 
        la $a0, msg5
        li $v0, printStr
        syscall 
        # printInt(value, 10); 
        move $a0, $t0
        li $a1, 10
        li $v0, printInt
        syscall 

        # printStr("\nValor em base 10 (unsigned), formatado: "); 
        la $a0, msg6
        li $v0, printStr
        syscall 
        # printInt(value, 10 | 5 << 16); // ver nota de rodapé 3 
        move $a0, $t0
        li $a1, 0x0005000A
        li $v0, printInt
        syscall 

        j main

        li $v0, 0
        jr $ra
        