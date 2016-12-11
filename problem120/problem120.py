if __name__ == '__main__':
	remainder = lambda a, n: ((a-1)**n + (a+1)**n) % a**2
	res = sum([max([remainder(a, n) for n in range(1, int(a*1.5)+1, 2)]) for a in range(3, 1001)])
	print('Result:', res)
