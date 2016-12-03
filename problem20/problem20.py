from functools import reduce
fact = lambda n: n*fact(n-1) if n > 1 else 1

if __name__ == '__main__':
	#print('Result:', sum([int(i) for i in str(fact(100))]))
	#print('Result:', reduce(lambda s,d: int(s)+int(d), str(fact(100))))
	print('Result:', sum(map(lambda d: int(d), str(fact(100)))))
