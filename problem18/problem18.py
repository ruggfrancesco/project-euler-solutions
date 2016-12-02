maxr = lambda r: [max(r[i],r[i+1]) for i in range(len(r)-1)]
sumr = lambda r, m: list(map(sum, zip(m, r)))

if __name__ == '__main__':
	triangle = open('triangle.txt', 'r').readlines()
	triangle = [i.strip().split() for i in triangle]
	triangle = [[int(j) for j in i] for i in triangle]
	
	for row in range(len(triangle)-1, 0, -1):
		triangle[row-1] = sumr(maxr(triangle[row]), triangle[row-1])
		
	print('Result:', triangle[0][0])
