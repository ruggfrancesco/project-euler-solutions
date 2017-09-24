from math import log10, floor
nlen = lambda n: floor(log10(n)+1)
nthdigit = lambda n,d: ((n % 10**d) - (n % 10**(d-1))) / 10**(d-1)

if __name__ == '__main__':
	fraction, lenght, prod = 0, 0, 1

	for rule in map(lambda x: 10**x, range(7)):
		while(lenght < rule):
			fraction += 1
			lenght += nlen(fraction)
		prod *= nthdigit(fraction, lenght-rule+1)
	
	print('Result:', int(prod))
