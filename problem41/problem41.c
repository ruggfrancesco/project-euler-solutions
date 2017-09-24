#include <stdio.h>
#include <math.h>

int factorials[10];

int fact(int n) {
	int prod = 1;
	for(int i=2; i<=n; i++)
		prod *= i;
	return prod;
}

int isprime(int a) {
 	if(a==2) return 1;
 	if(!(a % 2)) return 0;
 	for(int i=3; i<=sqrt(a); i+=2)
		if(!(a % i))
			return 0;
	return 1;
}

int getlen(int number) {
	return floor(log10(number)+1);
}

int is_pandigital(int n) {
	int len=getlen(n), sum=0, prod=1, tmp;

	while(n) {
		tmp = n % 10;
		sum += tmp;
		prod *= tmp;
		n /= 10;
	}
	
	return (sum==len*(len+1)/2 && prod==factorials[len]);
}

int main() {
	int pan = 87654321;
	for(int i=1; i<10; i++)
		factorials[i] = fact(i);
	
	while(!(is_pandigital(pan) && isprime(pan)))
		pan -= 2; //must be odd to be a prime
	
	printf("Result: %i\n", pan);
	return 0;
}
