from math import sqrt

isprime = lambda n: not any(filter(lambda x: not n%x, range(2, int(sqrt(n))+1)))

if __name__ == '__main__':
	primes = list(filter(isprime, filter(lambda x: len(set(str(x)))==3, range(1000, 10000))))
	
	for prime in primes:
		if prime+3330 in primes and prime+6660 in primes:
			if sorted(str(prime))==sorted(str(prime+3330))==sorted(str(prime+6660)):
				print('Result:', ''.join(str(prime)+str(prime+3330)+str(prime+6660)))
