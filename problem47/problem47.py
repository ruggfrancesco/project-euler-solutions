from math import sqrt
from time import time

cache_memory = dict()
t = time()

def memoization(F):
	def wrapper(*args):
		if tuple(args) not in cache_memory:
			cache_memory[tuple(args)] = F(*args)
		return cache_memory[tuple(args)]
	return wrapper

@memoization
def isprime(n):
	if n==2: return True
	if not n%2: return False
	for i in range(3, int(sqrt(n))+1, 2):
		if not n%i: return False
	return True

def prime_divisors(n):
	n_divisors = 0
	for i in range(2, int(n/2)+1):
		if not n%i and isprime(i):
			n_divisors += 1
	return n_divisors

if __name__ == '__main__':
	n = 134000
	cand = 0
	threshold = 4
	
	while cand != threshold:
		n += 1
		cand = cand+1 if prime_divisors(n)==threshold else 0
	
	print(list(range(n-(threshold-1), n+1)))
	print('Time elapsed: {0:.4f}s'.format(time()-t))