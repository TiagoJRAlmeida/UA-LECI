void exchange(char *c1, char *c2) {
    char aux = *c1;
    *c1 = *c2;
    *c2 = aux;
} 

char *strrev(char *str) {
    char *p1 = str;
    char *p2 = str;

    while(*p2 != '\0')
        p2++;
    p2--;

    while( p1 < p2 ) {
        exchange(p1, p2);
        p1++;
        p2--;
    }
    
    str = p2;
    return str;
} 

int main(void) {
    static char str[]="ITED - orievA ed edadisrevinU";

    printf("%s", strrev(str));
    return 0;
} 