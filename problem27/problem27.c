#include <stdio.h>
#include <math.h>

int isprime(int a) {
 	if (!(a % 2)) return 0;
 	for (int i = 3; i <= sqrt(a); i += 2)
		if (!(a % i))
			return 0;
	return 1;
}

int main() {
	int a, b, n, max_prod, max_step = 0, max_a, max_b;
	
	for (a = -61; a < 1000; a += 2) {
		for (b = 971; b < 1000; b++) {
			n = 0;
			while(isprime(n*n + a*n + b)) n++;
			if (n > max_step) {
				max_step = n;
				max_prod = a*b;
				max_a = a;
				max_b = b;
			}
		}
	}

	printf("Result: %i\n", max_prod); 
	return 0;
}
