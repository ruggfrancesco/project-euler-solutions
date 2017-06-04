from decimal import *

getcontext().prec=103
p, tot = 10**99, 0

for n in range(2,100):
	m = Decimal(n).sqrt()*p
	
	if m % 1 != 0:
		tot += sum([int(i) for i in str(m)[:100]])
	
print('Result:', tot)
