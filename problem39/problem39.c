#include <stdio.h>
#include <math.h>

int main() {
	int max_counter = 0, max_perimeter = 0;
	
	for (int perimeter = 5; perimeter <= 1000; perimeter++) {
		int counter = 0;
		for (int a = 1; a <= perimeter >> 2; a++)
			for (int b = a; b <= perimeter >> 1; b++)
				for (int c = b; c < perimeter >> 1; c+=2)
					if (a+b+c == perimeter && sqrt(a*a + b*b) == c)
						counter++;
		
		if (counter > max_counter) {
			max_counter = counter;
			max_perimeter = perimeter;
		}
	}

	printf("Result: %i\n", max_perimeter);
	return 0;
}
