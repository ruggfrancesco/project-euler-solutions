from math import sqrt

#isprime = lambda n: len(list(filter(lambda x: not n%x, range(2,int(sqrt(n))+1))))==0
nprimes = lambda row: len(list(filter(myisprime, row)))

def myisprime(n): #faster
	if n==2: return True
	if not n%2: return False
	for i in range(3, int(sqrt(n))+1, 2):
		if not n%i: return False
	return True

class spiral:
	def __init__(self, percentage):
		self.percentage = percentage
	
	def __iter__(self):
		self.diagonal = 1
		self.increment = 2
		self.diagonal_count = 1
		self.n_primes = 0
		return self

	def __next__(self):
		hop = [self.diagonal + i*self.increment for i in range(1, 5)]
		self.diagonal = hop[-1]
		self.n_primes += nprimes(hop)
		self.diagonal_count += 4
		self.increment += 2
		
		if (self.n_primes/self.diagonal_count) < self.percentage:
			print('Result:', int((self.diagonal_count+1)/2))
			raise StopIteration

if __name__ == '__main__':
	for hop in spiral(.1):
		pass
