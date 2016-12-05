def idigit(n):
	l = []
	while n:
		l.append(n%10)
		n //= 10
	return l

fact = lambda n: n*fact(n-1) if n>1 else 1

if __name__ == '__main__':
	#print('Result:', sum([i for i in range(3, 45000) if i==sum(map(lambda x: fact(x), idigit(i)))]))
	print('Result:', sum(filter(lambda n: n==sum(map(lambda d: fact(d), idigit(n))), range(3, 45000))))
