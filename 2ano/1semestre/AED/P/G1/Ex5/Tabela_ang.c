#include<stdio.h>
#include<math.h>

int main(void){
    int menor_ang;
    int maior_ang;
    int espacamento;
    float ang_rad;

    // Abrir/Criar o ficheiro de texto
    FILE * ficheiro = fopen("Tabela_ang.txt", "w");

    printf("Indique o menor angulo: ");
    scanf("%d", &menor_ang);
    printf("Indique o maior angulo: ");
    scanf("%d", &maior_ang);
    printf("Indique o espacamento entre angulos: ");
    scanf("%d", &espacamento);

    // Escrever para o ficheiro
    fprintf(ficheiro, "\n%s %s %12s\n", "ang", "sin(ang)", "cos(ang)");
    fputs("--- ------------ -----------", ficheiro);

    while(menor_ang <= maior_ang){
        ang_rad = menor_ang * (M_PI / 180.0);
        
        // Escrever para o ficheiro
        fprintf(ficheiro, "\n%3d %2.5lf %13.5lf", menor_ang, sin(ang_rad), cos(ang_rad));
        
        menor_ang += espacamento; 
    }

    // Fechar o ficheiro
    fclose(ficheiro);

    return 0;
}