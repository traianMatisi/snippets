#include <unistd.h>

void ft_print_alphabet(void){

    char c = 'a';

    while(c <= 'z'){
        write(1, &c, 1);
        c++;
    }

}
// MAIN.C //
/* 
#include "ft_print_alphabet.c"

void ft_print_alphabet(void);

int main(void){

    ft_print_alphabet();

    return 0;

}
 */
