#include <stdio.h>

int main(void){

    char tempo[4][6] = {"Anos", "Meses", "Dias"};
    int dias;
    int resto;
    int total;

    printf("Digite uma quantidade de dias: ");
    scanf("%i", &dias);

    for (int i = 0, j = 365; i < 3; i++, j -= 335){
        if(j < 0){
            total = resto;
        }else{
            resto = dias%j;
            total = dias/j;
            dias = resto;
        }
        printf("%s = %d\n", tempo[i], total);
    }
/* 
    resto = dias%365;
    total = dias/365;
    dias = resto;
    printf("Anos = %i\n", total);
    resto %= dias/30;
    total = dias/30;
    printf("Meses = %i\n", total);
    printf("Dias = %i\n", resto);
*/
    return 0;

}
