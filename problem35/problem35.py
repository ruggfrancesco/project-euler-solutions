from math import log10, floor

ndigit = lambda n: floor(log10(n))

def memoization(F):
	cache = dict()
	def wrapper(*args):
		if args not in cache:
			cache[args] = F(*args)
		return cache[args]
	return wrapper

@memoization
def isprime(n):
	if n==2: return True
	if not n%2: return False
	for d in range(3, int(n**.5)+1, 2):
		if not n%d: return False
	return True

rotate = lambda x: (x % 10**(ndigit(x)))*10 + (x // (10**ndigit(x)))

if __name__ == '__main__':
	res = 0
	
	for n in range(3, 10**6, 2):
		if isprime(n):
			r, c = n, 1
			nd = ndigit(n)
			for i in range(nd):
				r = rotate(r)
				if ndigit(r)==nd and isprime(r):
					c += 1
				else:
					break
			if c == nd+1:
				res += 1
	
	print('Result:', res + 1)
