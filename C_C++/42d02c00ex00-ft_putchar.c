#include <unistd.h>

void ft_putchar(char c){

    write(1, &c, 1);

}
// MAIN.C //
/* 
#include "ft_putchar.c"

void ft_putchar(char c);

int main(void){

    ft_putchar('z');

    return 0;

}
 */
