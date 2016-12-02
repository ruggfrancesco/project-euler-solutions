#include <stdio.h>
#include <math.h>

int divisors(int n) {
	int count=1;
	for(int i=2; i < round(sqrt(n))+1; i++) {
		if(!(n % i)) count++;
	}
	return count;
}

int nth_triangle(int n) {
	return (int)n*(n+1)/2;
}

int main() {
	for(int i=1; i<100000; i++)
		if(divisors(nth_triangle(i))*2+1 > 499) {
			printf("Result: %i\n", nth_triangle(i));
			return 0;
		}
	return 0;
}
