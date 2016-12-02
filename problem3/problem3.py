from math import sqrt

def isprime(n):
	if n==2: return True
	if not n%2: return False
	for i in range(3, int(sqrt(n))+1, 2):
		if not n%i: return False
	return True

def primediv(n):
	for i in range(int(sqrt(n))+1, 1, -2):
		if not n%i and isprime(i):
			return i

if __name__ == '__main__':
	print('Result:', primediv(600851475143))
