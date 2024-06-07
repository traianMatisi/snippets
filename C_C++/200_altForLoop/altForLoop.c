#include <stdio.h>

int main(void){
    
    int n = 10;

    for(int i = -1; i++ < n;){// supressed i++ in for's arg3
        printf("%i\n", i);
    }

    return 0;
}