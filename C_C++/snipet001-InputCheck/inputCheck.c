#include <stdio.h>

int main(void){

    int i = 0;
    char c = 's';

    do{

        do{
            printf("Digite um numero positivo: ");
            scanf("%i", &i);
            if(i < 0) printf("Numero invalido!\n");        
        }
        while(i < 0);

        printf("O numero digitado foi: %i\n", i);

        printf("Deseja digitar outro numero? [s/n]  ");
        scanf(" %c", &c);
    }
    while(c == 's');
    

    return 0;
    
}
