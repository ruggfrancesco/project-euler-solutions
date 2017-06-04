def search(mx):
	a,b = 0,1
	for i in range(mx):
		a=a+b
		b=b+a
		a,b = b,a
		yield(a,b)
		
if __name__ == '__main__':
	s = search(10)
	print(list(s))



