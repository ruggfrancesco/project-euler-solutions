divisorsof = lambda n: sum(filter(lambda d: not n%d, range(1,n//2+1)))

if __name__ == '__main__':
	divs = list(map(divisorsof, range(10001)))
	
	print('Result:', sum([i for i,j in enumerate(divs) if (j<10001 and i!=j and divs[j]==i)]))
