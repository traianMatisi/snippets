#include <stdio.h>

#define PI 3.1416

int main(void){
	
	float r, area;

	printf("Digite o raio do círculo: ");
	scanf("%f", &r);
	area = PI * r * r;

	printf("Area do circulo = %.3f\n", area);

	return 0;

}

