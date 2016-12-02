#include <stdio.h>
#include <math.h>

int main() {
 	int n = 100, x, y;
	
	x = pow((n+1)*(n/2), 2);
	y = n*(n+1)*(2*n+1)/6;
	
	printf("x = %i : y = %i\n", x, y);
	printf("Difference = %i\n", x - y);
	return 0;
}
