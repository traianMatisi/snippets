#include <stdio.h>

int main(void){

    char nome[20];
    float salario;
    float vendas;

    scanf("%s%f%f", nome, &salario, &vendas);

    salario = salario + (vendas * .15);

    printf("Salario %s = %.2f\n", nome, salario);

    return 0;
    
}
