from math import sqrt

def isprime(n):
	if n==2: return True
	if not n%2: return False
	
	for i in range(3, int(sqrt(n))+1, 2):
		if not n % i: return False
	return True

def sum_primes(mx):
	total_sum = 2 #2 because we start from 3
	for i in range(3, mx, 2):
		if isprime(i):
			total_sum += i
	return total_sum

if __name__ == '__main__':
	print('Result:', sum_primes(2000000))
