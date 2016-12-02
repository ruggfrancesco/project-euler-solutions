from math import sqrt

divisors = lambda n: len(list(filter(lambda x: not n % x, range(2, int(sqrt(n))+1))))
nth_triangle = lambda n: int(n*(n+1)/2)

def findtriangle(n):
	for i in range(n):
		if divisors(nth_triangle(i))*2+1 > 499:
			return nth_triangle(i)

if __name__ == '__main__':
	print('Result:', findtriangle(100000))
