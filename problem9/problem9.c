#include <stdio.h>

int main() {
	int a, b, c;
	
	for(a = 1; a <= 333; a++)
		for(b = 1; b <= 666; b++)
			for(c = 1; c <= 999; c++)
				if ((a + b + c == 1000) && (a*a + b*b == c*c)) {
					printf("a = %i\nb = %i\nc = %i\nResult: %i\n", a, b, c, a*b*c);
					break;
				}
	return 0;
}
