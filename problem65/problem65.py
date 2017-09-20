d,n = 1,2
	
for i in range(2,100):
	c = 2 * i / 3 if(not i % 3) else 1
	d, n = n, c*n + d

print("Result:", sum([int(dgt) for dgt in str(int(n*10))]))
