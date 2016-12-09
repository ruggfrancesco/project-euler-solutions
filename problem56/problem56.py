from math import log10
from functools import reduce

'''
def digit_sum(n):
	total = 0
	for i in range(int(log10(n))+1):
		total += n % 10
		n //= 10
	return total
'''

#Pythonic way
digit_sum = lambda n: sum(map(int, str(n)))

if __name__ == '__main__':
	print('Result:', max([digit_sum(i**j) for i in range(2,100) for j in range(2,100)]))
