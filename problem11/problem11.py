from functools import reduce

grid = open('grid', 'r').read().strip().split('\n')
grid = [[int(j) for j in i.split()] for i in grid]

treshold, highest = 3, 0
prod = lambda a,b: a*b

for y in range(len(grid)-treshold):
	for x in range(len(grid[y])-treshold):
		highest = max(highest, \
									*[reduce(prod, slc) \
									for slc in [
										 *[grid[y][x:x+3]],
											[grid[i][x] for i in range(y, y+4)],
											[grid[y+i][x+i] for i in range(4)],
											[grid[y+i][x-(i+1)] for i in range(4)]
										]
									])

		'''
		# A more readable (and almost equal) solution
		highest = max(highest,
									*[reduce(prod, *[grid[y][x:x+3]]),
										reduce(prod, [grid[i][x] for i in range(y, y+4)]),
										reduce(prod, [grid[y+i][x+i] for i in range(4)]),
										reduce(prod, [grid[y+i][x-(i+1)] for i in range(4)])
								])
		'''

print('Result:', highest)
