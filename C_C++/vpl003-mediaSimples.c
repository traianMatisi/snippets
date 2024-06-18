#include <stdio.h>

#define N 2 //define doesn't use = or ;

int main(void){

    float notas[N];
    float media;

    for (int i = 0; i < N; i++){
        scanf("%f", &notas[i]); // scanf is safe for integers
    }

    for (int i = 0; i < N; i++){
        media += notas[i];
    }    

    printf("Media = %.1f\n", media/N);
    
    return 0;
    
}
