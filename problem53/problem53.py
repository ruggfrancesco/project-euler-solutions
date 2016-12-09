from functools import reduce

def memoization(F):
	cache = dict()
	def wrapper(*args):
		if (F, args) not in cache:
			cache[(F, args)] = F(*args)
		return cache[(F, args)]
	return wrapper

#fact = lambda n: reduce(lambda x,y: x*y, range(2, n+1))

# Better use recursion for memoization ;D
@memoization
def fact(n):
	return 1 if n<=1 else n*fact(n-1)

n_ncr = lambda n: len(list(filter(lambda r: fact(n)/(fact(r)*fact(n-r)) > 10**6, range(1, n+1))))

if __name__ == '__main__':
	print('Result:', sum(map(lambda b: n_ncr(b), range(23, 101))))
