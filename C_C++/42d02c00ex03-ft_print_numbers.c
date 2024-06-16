#include <unistd.h>

void ft_print_numbers(void){

    char c = '0';

    while (c <= '9'){
        write(1, &c, 1);
        c++;
    }
    
}
// MAIN.C //
/* 
#include "ft_print_numbers.c"

void ft_print_numbers(void);

int main(void){

    ft_print_numbers();

    return 0;

}
 */
