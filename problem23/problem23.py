divisors = lambda n: sum(filter(lambda d: not n%d, range(2,int(n/2+1))))+1

if __name__ == '__main__':
	a = list(filter(lambda n: n<divisors(n), range(12, 28123)))
	s = {a[i]+a[j] for i in range(0, len(a)) for j in range(i, len(a))}

	print('Result:', sum(filter(lambda x: not x in s, range(1, 28123))))
