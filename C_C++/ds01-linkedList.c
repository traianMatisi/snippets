#include <stdio.h>
#include <stdlib.h>

typedef struct node{

    int data;
    struct node *next;

}node;

void insertValue(char a);

int main(int argc, char **argv){

    printf("Running linkedList.c\n");

    int n = 5;
    char c = 64;
    node *list = NULL;/*garbage values are bad for pointers*/

    for (int i = 0; i < n; i++)
    {
        insertValue(++c);
    }
        

    

    return 0;
}

void insertValue(char a){

    node *tmpNode = malloc(sizeof(node));

    if(tmpNode != NULL){
    
        tmpNode->data = a; // (*tmpNode).data = a;
        tmpNode->next = NULL; // (*tmpNode).next = NULL;

    }
    else{
        printf("Error inserting node\n");
    }


}