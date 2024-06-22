/*
SOMA
Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variável X. Imprima X conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que está sendo especificado.
Entrada
A entrada contém 2 valores inteiros.
Saída
Imprima a variável X conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. Obs: O X está em maiúsculo e deve ter um espaço antes e um espaço depois do sinal de igualdade.

Exemplos
10
9
X = 19

-10
4
X = -6

15
-7
X = 8
 */

#include <stdio.h>

int main(void){
	int a = 0, b = 0;
	scanf("%i%i", &a, &b);
	int x = a + b;
	printf("X = %i", x);
	return 0;
}
