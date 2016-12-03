from functools import reduce

if __name__ == '__main__':
	names = open('p022_names.txt', 'r').read().split("\"")
	names = sorted([name for name in names if name and name != ','])
	
	print('Result:', sum([reduce(lambda x,y: x+y, map(lambda d: ord(d)-64, name)) * (ind+1) for ind,name in enumerate(names)]))
	
	'''
	#Readable version:
	s = 0
	for index,name in enumerate(names):
		s += reduce(lambda x,y: x+y, map(lambda d: ord(d)-64, name)) * (index+1)
	print('Result:', s)
	'''
