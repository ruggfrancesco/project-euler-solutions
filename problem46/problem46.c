#include <stdio.h>
#include <stdlib.h>

isprime(int a) {
	if(a==2) return 1;
 	if (!(a % 2)) return 0;
 	int i;
 	for (i = 3; i <= sqrt(a); i += 2)
		if (!(a % i))
			return 0;
	return 1;
}

int issquare(int n) {
	return (int)sqrt(n)==(float)sqrt(n);
}

void main() {
	int comp = 3, flag = 1, primes[10000], i = 1, k = 1, sum, sqr, found;
	
	primes[0] = 2;
	while (i < 10000) {
		k += 2;
		if (isprime(k)) primes[i++] = k;
	}
	
	while (flag) {
		comp++;
		if (!isprime(comp) && (comp % 2)) {
			found = 0;
			
			i = 0; sum = 1;
			while (i >= 0 && !found) {
				sum = comp - primes[i];
				if (sum >= 0) {
					if (!(sum % 2)) {
						sqr = sum / 2;
						if (issquare(sqr))
							found = 1;
					}
					i++;
				}
				else
					i = -1;
			}
			if (!(found)) {
				printf("Result: %i\n", comp);
				flag = 0;
			}
		}

	}
	
}
