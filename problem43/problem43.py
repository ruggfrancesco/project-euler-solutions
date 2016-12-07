from itertools import permutations
from math import log10, floor

subn = lambda l,d: int(''.join(map(lambda i: l[i], range(d, d+3))))

if __name__ == '__main__':
	rules, res = [2,3,5,7,11,13,17], 0
	
	for perm in permutations('1406375289'):
		if not any([subn(perm, d+1) % rule for d,rule in enumerate(rules)]):
			res += int(''.join(perm))

	'''	
	#this one is more efficient because we
	#suddenly stop if a rule is not followed
	for perm in permutations('1406375289'):
		for d,rule in enumerate(rules):
			if subn(perm, d+1) % rule: break
			d+=1
		
		if d==7:
			res += int(''.join(perm))
	'''
	
	print('Result:', res)
