from decimal import *
getcontext().prec = 102

def digitSum(n):
	r = str(Decimal(n**Decimal(.5)))[:101].replace('.','')
	s = sum(map(int, r))
	return s if s > 10 else 0

res = sum(map(digitSum, range(2,100)))
print('Result:', res)
