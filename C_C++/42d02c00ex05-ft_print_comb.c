#include <unistd.h>

void ft_print_comb(void){

    char comb[3] = {'/', '/', '/'};// TODO optimize

    for(comb[0] = 48; comb[0] <= 55; comb[0]++){
        for(comb[1] = comb[0]+1; comb[1] <= 56; comb[1]++){
            for(comb[2] = comb[1]+1; comb[2] <= 57; comb[2]++){

                for (int i = 0; i < 3; i++){
                    write(1, &comb[i], 1);
                }
                write(1, ",", 2);
            }
        }
    }    
}
// MAIN.C //
/* 
#include "ft_print_comb.c"

void ft_print_comb(void);

int main(void){

    ft_print_comb();
    
    return 0;

}
 */
