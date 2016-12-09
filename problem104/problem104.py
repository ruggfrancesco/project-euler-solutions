from itertools import permutations

def fibgen():
	a, b = 1, 0
	while True:
		yield a
		a, b = a+b, a

#pythonic way
ispandigital = lambda n: len(str(n))==9 and all(map(lambda i: str(i) in str(n), range(1,10)))

#slightly faster
'''
def ispandigital(x):
	if len(str(x)) != 9: return False
	for i in range(1,10):
		if str(i) not in str(x):
			return False
	return True
'''

check = lambda n: ispandigital(n % 10**9) and ispandigital(n // 10**(len(str(n))-9))

if __name__ == '__main__':
	k, fib = 1, fibgen()
	while not check(next(fib)):
		k += 1

	print('Result:', k)
