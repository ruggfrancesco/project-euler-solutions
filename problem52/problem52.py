check_equal = lambda l:	len(set([''.join(sorted(str(i))) for i in l]))==1

def loop(n=10):
	while(not check_equal([n*i for i in range(1, 7, 2)])):
		n += 1
	return n

if __name__ == '__main__':
	print('Result:', loop())
