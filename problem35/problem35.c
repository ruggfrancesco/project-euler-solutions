#include <stdio.h>
#include <math.h>

int getlen(number) {
	int i=1;
	while(number /= 10) i++;
	return i;
}

int permutations(int number, int k) {
	return number/10 + ((number % 10) * pow(10,k-1));
}

int isprime(int n) {
	if (!(n%2)) return 0;
	for (int i=2; i<=sqrt(n); i++)
		if (n % i == 0) return 0;
	return 1;
}

int main() {
	int number = 100, k, r, counter = 13, perm;

	while(++number < 1000000) {
		perm = number;
		k = getlen(number);
				
		if (isprime(number))
			for (int i = 1; i < k; i++)
				if(isprime(perm = permutations(perm, k))) r++;
		
		if (r == k-1)
			counter++;
		r = 0;
	}
	
	printf("Result: %i\n", counter);
	return 0;
}



