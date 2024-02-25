#include <detpic32.h>

int main(void){ 
    char c; 
    int cnt = 0; 
 
    do { 
        c = inkey(); 
        if( c != 0 ) 
            putChar( c ); 
        else 
            putChar('.'); 
        cnt++; 
    } while( c != '\n' ); 
    
    printInt(cnt, 10); 
    return 0; 
}