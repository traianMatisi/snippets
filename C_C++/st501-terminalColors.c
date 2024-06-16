#include <stdio.h>

int main(int argc, const char**argv){
	char font[] = "\e[1;33m";
	char background[] = "\e[1;41m";
	char reset[] = "\e[m";
	printf("%s%s Hello, friend... %s\n", font, background, reset);
	return 0;
}

