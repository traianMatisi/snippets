#include <unistd.h>

void ft_print_comb2(void){

    char arr[7] = {'0', '0', ' ', '0', '0', ',', ' '};

    for (arr[0] = '0'; arr[0] <= '9'; arr[0]++){
        for (arr[1] = '0'; arr[1] <= '9'; arr[1]++){
            for (arr[3] = '0'; arr[3] <= '9'; arr[3]++){
                for (arr[4] = '0'; arr[4] <= '9'; arr[4]++){

                    if(arr[0] == '9' && arr[1] == '9' && arr[3] == '9' && arr[4] == '9'){
                        write(1, &arr, 5);
                        write(1, "\n", 1);// '\n' will try to print an int
                    }
                    else{
                        write(1, &arr, 7);
                    }

                }                
            }
        }        
    }
}
