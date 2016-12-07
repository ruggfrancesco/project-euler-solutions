#include <stdio.h>
#include <stdlib.h>

isprime(int a) {
 	if(a==2) return 1;
 	if(!(a % 2)) return 0;
 	for(int i = 3; i <= sqrt(a); i += 2)
		if(!(a % i))
			return 0;
	return 1;
}

int issquare(int n) {
	return sqrt(n) == (float)sqrt(n);
}

void main() {
	int comp = 3, flag = 1, primes[10000], i = 1, k = 1, sum, sqr, found;
	
	while (i < 10000)
	{
		k += 2;
		if (isprime(k)) primes[i++] = k;
	}
	
	while (flag)
	{
		comp++;
		if (!isprime(comp) && (comp % 2))
		{
			// Now we have a composite number. Just test if it can be written as the sum of a prime and twice a square;
			found = 0;
			
			// Substract su comp each prime number until it goes under 0 or we have found a solution;
			i = 0; sum = 1;
			while (i >= 0 && !found)
			{
				sum = comp - primes[i];
				if (sum >= 0)
				{
					//	At this point we need to figure out if sum is a twice square (obviously if it's even);
					if (!(sum % 2))
					{
						sqr = sum / 2;
						
						if (issquare(sqr))
						{
							printf("%i = %i + %i", comp, primes[i], sum);
							printf("\t->\t%i -> 2 * %i", sum, sqr);
							printf("\t->\t%i is a perfect square\n", sqr);
							found = 1;
						}
					}
					i++;
				}
				else
					i = -1;
			}
			if (!(found))
			{
				printf("Solution: %i\n", comp);
				flag = 0;
			}
		}

	}
	
}
