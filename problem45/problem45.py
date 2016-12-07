from functools import reduce

class triangle:
	def __init__(self):
		self.n = 285
	def __iter__(self):
		return self
	def __next__(self):
		self.n += 1
		return int(self.n*(self.n+1)/2)

class pentagonal:
	def __init__(self):
		self.n = 165
	def __iter__(self):
		return self
	def __next__(self):
		self.n += 1
		return int(self.n*(self.n*3-1)/2)

class hexagonal:
	def __init__(self):
		self.n = 143
	def __iter__(self):
		return self
	def __next__(self):
		self.n += 1
		return int(self.n*(self.n*2-1))

if __name__ == '__main__':
	series = [[{next(triangle())}, triangle()], [{next(pentagonal())}, pentagonal()], [{next(hexagonal())}, hexagonal()]]

	while True:
		for serie in series:
			[serie[0].add(next(serie[1])) for i in range(100)]
		if series[0][0].intersection(series[1][0].intersection(series[2][0])):
			print('Result:', *series[0][0].intersection(series[1][0].intersection(series[2][0])))
			break
