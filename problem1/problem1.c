#include <stdio.h>

void main() {
	int i, sum = 0;
	for (i = 1; i < 1000; i++)
		if (!(i % 3) || !(i % 5))
			sum += i;

	printf("Result: %i\n", x);
}
