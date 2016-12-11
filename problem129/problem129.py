from fractions import gcd

def A(n):
	if gcd(n, 10) != 1: return 0
	
	x, k = 1, 1
	
	while x:
		x = (x*10 + 1) % n
		k+=1
	return k

if __name__ == '__main__':
	limit = 1000001
	n = limit
	
	while(A(n) < limit):
		n += 2
	
	print('Result:', n)
