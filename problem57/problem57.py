check = lambda a,b: len(str(a))>len(str(b))

def expand(n):
	cnt, a, b = 0, 3, 2
	for i in range(n):
		b, a = a+b, a+2*b
		if a>b and check(a,b): cnt += 1
	return cnt

if __name__ == '__main__':
	print('Result:', expand(1000))
