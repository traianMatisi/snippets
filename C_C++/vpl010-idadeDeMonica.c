/*
A IDADE DE MONICA
Dona Mônica é mãe de três filhos que têm idades diferentes. Ela notou que, neste ano, a soma das idades dos seus três filhos é igual à idade dela. Neste problema, dada a idade de dona Mônica e as idades de dois dos filhos, seu programa deve computar e imprimir a idade do filho mais velho.

Por exemplo, se sabemos que dona Mônica tem 52 anos e as idades conhecidas de dois dos filhos são 14 e 18 anos, então a idade do outro filho, que não era conhecida, tem que ser 20 anos, pois a soma das três idades tem que ser 52.

Portanto, a idade do filho mais velho é 20. Em mais um exemplo, se dona Mônica tem 47 anos e as idades de dois dos filhos são 21 e 9 anos, então o outro filho tem que ter 17 anos e, portanto, a idade do filho mais velho é 21.

Entrada
A primeira linha da entrada contém um inteiro M representando a idade de dona Mônica.  A segunda linha da entrada contém um inteiro A representando a idade de um dos filhos. A terceira linha da entrada contém um inteiro B representando a idade de outro filho.

Saída
Seu programa deve imprimir uma linha, contendo um número inteiro, representando a idade do filho mais velho de dona Mônica.

Restrições
40<= M <= 110
1 <= A < M
1 <= B < M
A != B

Exemplo de entrada 1
52
14
18
Exemplo de saída 1
20

Exemplo de entrada 2
47
21
9
Exemplo de saída 2
21
*/

#include <stdio.h>

int main(){
    int monica, filho_a, filho_b, filho_c;
    do{
        printf("Idade Monica --> ");
        scanf("%i", &monica);
    }while(monica < 40 || monica > 110);
    do{
        printf("Idade filho A --> ");
        scanf("%i", &filho_a);
    }while(filho_a >= monica);
    do{
        printf("Idade filho B --> ");
        scanf("%i", &filho_b);
    }while(filho_b >= monica && filho_b == filho_a);
    filho_c = monica - filho_a - filho_b;
    printf("Monica: %i\nFilho A: %i\nFilho B: %i\nFilho C: %i\n", monica, filho_a, filho_b, filho_c);
    printf("Filho mais velho --> ");
    if (filho_a > filho_b && filho_a > filho_c) printf("%i", filho_a);
    else if(filho_b > filho_c) printf("%i", filho_b);
    else printf("%i", filho_c);
    return 0;
}