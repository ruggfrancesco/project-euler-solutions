from itertools import permutations

nthdigit  = lambda n, d: int(((n % 10**d) - (n % 10**(d-1))) / 10**(d-1))
getdigits = lambda p, i: [nthdigit(int(''.join(p)), 11-j) for j in range(i, i+3)]
listtoint = lambda l: int(''.join(map(str, l)))

if __name__ == '__main__':
	rules, res = [2,3,5,7,11,13,17], 0
	
	for perm in permutations('0123456789'):
		divs = 2
		for rule in rules:
			dd = getdigits(perm, divs)
			nn = listtoint(dd)
			if nn % rule: break
			divs += 1
		
		if divs==9:
			res += listtoint(perm)
			print('found:', ''.join(perm), dd, nn, rule)
			print('Result:', res)

