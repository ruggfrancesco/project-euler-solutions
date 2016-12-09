from math import floor, log10
from itertools import permutations

def memoization(F):
	cache = dict()
	def wrapper(*args):
		if args not in cache:
			cache[args] = F(*args)
		return cache[args]
	return wrapper

nlen = lambda n: floor(log10(n)+1)
merge = lambda x,y: int(x*10**nlen(y)+y)

@memoization
def myisprime(n):
	if n==2: return True
	if not n%2: return False
	for i in range(3, int(n**.5)+1, 2):
		if not n%i: return False
	return True

def check(comb):
	for perm in permutations(comb, 2):
		if not myisprime(merge(*perm)):
			return False
	return True

#this function is ugly but it's pretty fast
def findset():
	for a in range(len(primes)):
		for b in range(a+1, len(primes)):
			if check([primes[a], primes[b]]):
				for c in range(b+1, len(primes)):
					if check([primes[a], primes[b], primes[c]]):
						for d in range(c+1, len(primes)):
							if check([primes[a], primes[b], primes[c], primes[d]]):
								for e in range(d+1, len(primes)):
									if check([primes[a], primes[b], primes[c], primes[d], primes[e]]):
										return sum([primes[a], primes[b], primes[c], primes[d], primes[e]])

if __name__ == '__main__':
	primes = list(filter(lambda n: myisprime(n), range(3, 10000)))
	print('Result:', findset())
