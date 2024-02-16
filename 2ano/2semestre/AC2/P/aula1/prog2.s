# int main(void) {
#     char c;
#     int cnt = 0;
#     do {
#        c = getChar();
#        putChar( c );
#        cnt++;
#     } while( c != '\n' );
#     printInt(cnt, 10);
#     return 0;
# }

        .data
        .equ printInt10, 7
        .equ getChar, 2
        .equ putChar, 3
        .text
        .globl main

main:   li $t0, 0 # cnt = 0;
        
do:     li $v0, getChar
        syscall
        move $a0, $v0
        li $v0, putChar
        syscall
        addi $t0, $t0, 1 
        bne $a0, '\n', do

edo:    move $a0, $t0
        li $v0, printInt10
        syscall
        li $v0, 0
        jr $ra