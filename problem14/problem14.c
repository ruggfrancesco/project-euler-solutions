#include <stdio.h>

int main() {
	long int n=0;
	int current_chain, longest_chain=0, max_chain_number;

	for(int i=1; i<1000000; i++) {
		n = i;
		current_chain = 1;
		
		while(n != 1) {
			if(n % 2 == 0)
				n /= 2;
			else
				n = 3*n + 1;
			current_chain++;
		}

		if(current_chain > longest_chain) {
			longest_chain = current_chain;
			max_chain_number = i;
		}
	}
	printf("Result: %li\n", max_chain_number);
	return 0;
}
