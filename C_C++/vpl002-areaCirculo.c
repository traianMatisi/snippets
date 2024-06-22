/* 
ÁREA DO CÍRCULO
A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:
- Efetue o cálculo da área, elevando o valor de Raio ao quadrado e multiplicando por π.
Entrada
A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
Saída
Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double).


Exemplos:
2.00
A=12.5664

100.64
A=31819.3103


150.00

A=70685.7750
*/

#include <stdio.h>

#define PI 3.14159

int main(void){
	double r, a;
	scanf("%lf", &r);
	a  = PI * r * r;
	printf("A=%.4lf", a);
	return 0;
}
