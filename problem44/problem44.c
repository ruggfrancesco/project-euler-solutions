#include <stdio.h>
#define max 3000

int binary_search(int a[], int n, int key) {
	int down = 0, up = n-1, pos;
	while(down < up) {
		if (key != a[pos]) {
			pos = (down + up) / 2;
			if(key > a[pos])
				down = pos + 1;
			else if(key < a[pos])
				up = pos;
		}
		else return 1;
	}
	return 0;
}

int main() {
	int n, pent[50000];
	
	for (n = 1; n < max; n++)
		pent[n] = n*(3*n-1)/2;	
	
		for (int i = 1; i < n; i++)
			for (int j = i+1; j < n; j++)
				if (binary_search(pent, n, pent[i]+pent[j]) && binary_search(pent, n, pent[j]-pent[i])) {
					printf("Result: %i\n", pent[j]-pent[i]);
					return 1;
				}
	return 0;
}
