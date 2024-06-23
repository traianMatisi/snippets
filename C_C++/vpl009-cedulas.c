/*
CÉDULAS
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido.

Exemplos
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00

11257
11257
112 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
0 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
1 nota(s) de R$ 2,00
0 nota(s) de R$ 1,00

503
503
5 nota(s) de R$ 100,00
0 nota(s) de R$ 50,00
0 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
0 nota(s) de R$ 5,00
1 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
*/

#include <stdio.h>

int main(){
    int notas, notas100, notas50, notas20, notas10, notas5, notas2, notas1;
    //scanf("%i", &notas);
    notas = 188;
    notas100 = notas / 100;
    notas %= 100;
    notas50 = notas / 50;
    notas %= 50;
    notas20 = notas / 20;
    notas %= 20;
    notas10 = notas / 10;
    notas %= 10;
    notas5 = notas / 5;
    notas %= 5;
    notas2 = notas / 2;
    notas %= 2;
    notas1 = notas;
    printf("%i nota(s) de R$ 100,00\n%i nota(s) de R$ 50,00\n%i nota(s) de R$ 20,00\n%i nota(s) de R$ 10,00\n%i nota(s) de R$ 5,00\n%i nota(s) de R$ 2,00\n%i nota(s) de R$ 1,00\n", notas100, notas50, notas20, notas10, notas5, notas2, notas1, notas);
    return 0;
}
