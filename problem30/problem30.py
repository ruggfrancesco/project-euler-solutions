from functools import reduce

def idigit(n):
	l = []
	while n:
		l.append(n%10)
		n //= 10
	return l

if __name__ == '__main__':
	s = 0
	for i in range(1, 2*10**5):
		if i==sum(map(lambda x: x**5, idigit(i))):
			s+=i
	print('Result:', s)
