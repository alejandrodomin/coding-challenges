#include <stdio.h>

void hex_dump(char*);

int main() {
	char str[] = "Hello worldbob\n";
	
	hex_dump(&str);
	
	return 0;
}

void hex_dump(char* ptr) {
	int ipL=30;
	char line[ipL];
	//ptr=0x0; immediate segmentation fault since you're trying to access the outside the program

	int i = 0;
	printf("%05p| ", &ptr);
	for(i; i < 10000; i++) {
		unsigned char value = *ptr++;
		printf("%02x ", value);

		if(value == '\n' || value > 0x7F)
			line[i%ipL]=' ';
		else 
			line[i%ipL]=value;

		if((i + 1) % ipL == 0) {
			printf("|%s\n", line);	
		  printf("%05p| ", &ptr + i);	
		}
	}

	printf("\n");	
}
