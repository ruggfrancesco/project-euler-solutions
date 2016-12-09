def memoization(F):
	cache = dict()
	def wrapper(*args):
		if args not in cache:
			cache[args] = F(*args)
		return cache[args]
	return wrapper

@memoization
def isprime(n):
	return not any(filter(lambda x: not n%x, range(2, int(n**.5)+1)))

if __name__ == '__main__':
	primes = list(filter(lambda n: isprime(n), range(4*10**3)))
	
	print('Result:', max([(j-i, sum(primes[i:j])) for i in range(len(primes)) for j in range(len(primes),i+1,-1) if sum(primes[i:j])<10**6 and isprime(sum(primes[i:j]))], key=lambda e: e[0])[1])
