from functools import reduce

def fibgen(mx):
	a, b = 0, 1
	s = 0
	while a<mx:
		yield a
		a, b = a+b, a

print('Result:', reduce(lambda x,y: x+y, filter(lambda x: not x%2, fibgen(4000000))))
