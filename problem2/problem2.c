#include <stdio.h>

void main() {
	int a=0, b=1, c, sum=0;
	while (sum < 4000000) {
		c = a;
		a = a + b;
		b = c;
		sum += a%2 ? a : 0;
	}

	printf("Result: %i\n", sum);
}
