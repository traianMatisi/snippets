#include <stdio.h>

int main(void){

	int x, y, soma;

	printf("Digite o #1 valor: ");
	scanf("%i", &x);
	printf("Digite o #2 valor: ");
	scanf("%i", &y);
	soma = x + y;

	printf("%i + %i = %i\n", x, y, soma);

	return 0;

}

