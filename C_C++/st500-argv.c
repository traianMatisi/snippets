#include "ft_putchar.c"

void ft_putchar(char c);

int main(int argc, char**argv){

    char c = '\n';

    for(int i = 1; i < argc; i++){

        for(int j = 0; argv[i][j] != '\0'; j++){
            ft_putchar(argv[i][j]);
        }

        write(1, &c, 1);

    }
    
}
// FT_PUTCHAR.C //
/* 
#include <unistd.h>

void ft_putchar(char c){
    write(1, &c, 1);
}
 */
