#include <stdio.h>

int getlen(int number) {
	int i = 1;
	while (number /= 10) i++;
	return i;
}

int ispalindrome(int a[], int x) {
	int i, inf = 0, n = getlen(x), sup = n - 1;
	
	for (i = 0; i < n; i++) {
		a[i] = x % 10;
		x /= 10;
	}

	while (inf < sup)
		if (a[inf] == a[sup]) {
			inf++;
			sup--;
		}
		else
				return 0;
	return 1;
}
	
int main() {
	int x, y, n, max, a[6];
	
	x = y = 999;
	
	for (x = 999; x > 100; x--)
		for (y = 999; (y > 100) && (n = x * y); y--)
			if (ispalindrome(a, x * y) && (max < n)) {
				max = x * y;
				break;
			}
	
	printf("Result: %i\n", max);
	return 0;
}
