# int main(void){
#     char c;
#     int cnt = 0;
#     do {
#         c = inkey();
#         if( c != 0 )
#             putChar( c );
#         else
#             putChar('.');
#         cnt++;
#     } while( c != '\n' );
#     printInt(cnt, 10);
#     return 0;
# }
###############################################

        .data
        .equ inkey, 1
        .equ getChar, 2
        .equ putChar, 3
        .equ printInt10, 7
        .text
        .globl main

main:   li $t0, 0 # cnt = 0

do:     li $v0, inkey
        syscall
        move $t1, $v0  # c = inkey()

if:     beq $t1, 0, else
        move $a0, $t1
        li $v0, putChar
        syscall
        j edo

else:   lb $t1, '.'
        move $a0, $t1
        li $v0, putChar
        syscall
        j edo


edo:    addi $t0, $t0, 1 
        bne $t1, '\n', do

eloop:  move $a0, $t0
        li $v0, printInt10
        syscall
        li $v0, 0
        jr $ra


