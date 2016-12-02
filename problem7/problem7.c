#include <stdio.h>
#include <math.h>

int isprime(int a) {
 	if (a == 2) return 1;
 	if (!(a % 2)) return 0;
 	for (int i = 3; i <= (int)sqrt(a); i += 2)
		if (!(a % i))
			return 0;
	return 1;
}

int main() {
	int n = 1, count = 0;
	while (count < 10000) {
		n += 2;
		if (isprime(n)) count++;
	}
	
	printf("10001st prime number is: %i\n", n);
	return 0;
}

