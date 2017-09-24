#include <stdio.h>
#include <math.h>

int getlen(int number) {
	return floor(log10(number)+1);
}

int comb_right(int n) {
	return (n - (n % 10))/10;
}

int comb_left(int n) {
	return n % (int)(pow(10,getlen(n)-1));
}

int isprime(int n) {
	if (n==1 || n==2) return n-1;
	if (!(n % 2)) return 0;
	for (int i=3; i<=sqrt(n); i+=2)
		if(!(n % i)) return 0;
	return 1;
}

int main() {
	int i, number = 9, counter = 0, sum = 0;
	while (counter < 11) {
		number += 2;
		if (isprime(number)) {
			int len = getlen(number);
			int perm = number;
			
			for (i = 0; i < len; i++) {
				perm = comb_right(perm);
				if (!isprime(perm)) break;
			}
			
			if (i == len-1) {
				perm = number;	
				for (i = 0; i < len; i++) {
					perm = comb_left(perm);
					if (!isprime(perm)) break;
				}
			}
			
			if (i == len-1) {
				counter++;
				sum += number;
			}		
		}
	}
	
	printf("Result: %i\n", sum);
	return 0;
}
