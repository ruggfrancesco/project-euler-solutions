#include <stdio.h>
#include <math.h>

int isprime(int x) {
 	if (!(x % 2)) return 0;
 	for (int i = 3; i <= sqrt(x); i+=2)
		if (!(x % i)) return 0;
	return 1;
}

int main() {
	long int total = 2;
	
	for (int x=3; x < 2000000; x+=2)
		if(isprime(x)) total += x;
	
	printf("Result: %li\n", total);
	return 0;
}
