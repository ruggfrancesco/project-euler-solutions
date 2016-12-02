#include <stdio.h>
#include <math.h>

int isprime(long int x) {
	if (!(x % 2)) return 0;
	for (int i = 3; i < (int)sqrt(x); i++)
		if (!(x % i)) return 0;
	return 1;
}

int main() {
	long int x = 600851475143;
	
	for(int i = sqrt(x)+1; i>0; i-=2)
		if (!(x % i) && isprime(i)) {
			printf("Result: %lli\n", i);
			return 0;
		}
}
