#include <unistd.h>

void ft_putnbr(int nb){

    int n[10]; // unsigned int goes as high as 4 294 967 295, 10 digit number

    for(int i = 9; i >= 0; nb /= 10, i--){
        n[i] = 48 + (nb % 10);
    }

    for (int i = 0; i <= 9; i++){
        if(n[i]){
            /* code */
        }
        
        write(1, &n[i], 1);
    }

    write(1, "\n", 1);

}
// MAIN.C //
/*
#include "ft_putnbr.c"

void ft_putnbr(int nb);

int main(void){
    ft_putnbr(42);
    return 0;
}
 */
