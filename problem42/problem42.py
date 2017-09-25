from math import floor

ordsum = lambda word: sum(map(lambda l: ord(l)-64, word))
istriangle = lambda n: floor((8*n+1)**.5)==(8*n+1)**.5

if __name__ == '__main__':
	words = open('words.txt').read().split('-')
	print('Result:', len(list(filter(lambda word: istriangle(ordsum(word)), words))))
