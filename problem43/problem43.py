from itertools import permutations
from math import log10, floor

getint = lambda l: int(''.join(map(str, l)))
lenn = lambda n: floor(log10(n)+1)
subn = lambda n, f,t: int(((n % 10**(lenn(n)-f+1)) - (n % 10**(lenn(n)-t+1))) / 10**(lenn(n)-t+1))

if __name__ == '__main__':
	rules, res = [2,3,5,7,11,13,17], 0
	
	for perm in permutations(range(10)):
		for d,rule in enumerate(rules):
			pi = getint(perm)
			if subn(pi, d+2,d+5) % rule: break
		if d==6:
			res += pi
			print(pi)
	print('Result:', res)
