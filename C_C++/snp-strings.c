#include <stdio.h>

int main(int argc, char **argv){

    char zero = 'z';
    printf("%c\n", zero);

    char nome[] = "Traian Matisi";
    printf("%s\n", nome);

    // 5 elementos de 6 letras + 1 letra (\0)
    char nomeCompleto[5][7] = {"de", "Lima", "Vaz", "Traian", "Matisi",};

    for(int i = 0; i < 5; i++){
        printf("%s\n", nomeCompleto[i]);
    }

    for(int i = 0; i < argc; i++){
        for(int j = 0; argv[i][j] != '\0'; j++){
            printf("%c", argv[i][j]);
        }
        printf("\n");
    }    
    return 0;
}
