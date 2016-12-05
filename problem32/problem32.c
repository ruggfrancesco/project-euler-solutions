#include <stdio.h>
#include <math.h>

int getlen(int number) {
	int i = 1;
	while (number /= 10) i++;
	return i;
}

int is_pandigital(int x) {
	int i, j, a[10], len = getlen(x), sum = 0;

	for (i = 0; i < len; i++) {
		a[i] = x % 10;
		x /= 10;
	}
	
	for (i = 0; i < len; i++) sum += a[i];
	
	if (sum == len*(len+1)/2) {
		for (i = 0; i < len; i++)
			for (j = i+1; j < len; j++)
				if (a[i] == a[j]) return 0;
		return 1;
	}
	else return 0;
}

int ricerca(long int a[], long int chiave, long int n) {
	for (long int i=0; i <= n; i++)
		if (a[i] == chiave)
			return 0;
	return 1;
}

int main() {
	long int a, b, c, prod, t_len, len_a, len_b, len_c, array[1000], counter = 0, sum = 0;
	
	for (a = 1; a < 9000; a++)
		for (b = 1; b < 9000; b++) {
			c = a * b;
			if (c <= 987654321) {
				len_a = getlen(a); len_b = getlen(b); len_c = getlen(c);
				t_len = len_a + len_b + len_c;
				if (t_len == 9) {
					prod = a * pow(10, (t_len - len_a)) + b * pow(10, (t_len - len_a - len_b)) + c * pow(10, (t_len - len_a - len_b - len_c));
					if (is_pandigital(prod) && ricerca(array, c, counter)) {
						array[counter++] = c;
						sum += c;
					}
				}
			}
			else b = 9000;
		}


	printf("Result: %i\n", sum);
	return 0;
}

