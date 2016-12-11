cache_memory = dict()

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
	for i in range(3, int(n**.5)+1, 2):
		if not n%i: return False
	return True

def prime_divisors(n):
	n_divisors = 0
	for i in range(2, int(n/2)+1):
		if not n%i and isprime(i):
			n_divisors += 1
	return n_divisors

if __name__ == '__main__':
	n, cand, dfactors= 134000, 0, 4
	
	while cand != dfactors:
		n += 1
		cand = cand+1 if prime_divisors(n)==dfactors else 0
	
	print('Result:', n-3)
