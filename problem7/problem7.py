from math import sqrt

def isprime(n):
	if n==2: return True
	if not n%2: return False
	
	for i in range(3, int(sqrt(n))+1, 2):
		if not n % i: return False
	return True

def nth_prime(mx):
	count = 1 #1 because we exclude 2 from the count
	candidate = 1
	while count < mx:
		candidate+=2
		if isprime(candidate): count += 1	

	return candidate

if __name__ == '__main__':
	print('10001st prime number is:', nth_prime(10001))
