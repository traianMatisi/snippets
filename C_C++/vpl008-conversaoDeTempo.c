/*
CONVERSÃO DE TEMPO
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

Exemplos
556
0:9:16

1
0:0:1

140153
38:55:53
*/

#include <stdio.h>

int main(){
    int segundos, minutos, horas;
    scanf("%i", &segundos);
    horas = segundos / 3600;
    segundos %= 3600;
    minutos = segundos / 60;
    segundos %= 60;
    printf("%i:%i:%i\n", horas, minutos, segundos);
    return 0;
}
