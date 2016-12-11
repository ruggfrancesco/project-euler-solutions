import functools

def lc_gen(k, t=0):
	pw2 = (1 << 19)
	for i in range(1, k+1):
		t = (615949*t + 797807) % 2**20
		sk = t - pw2
		yield sk

def gen_triangle(lst, i=0, j=0, k=0):
	triangle = []
	while(j+i < len(lst)):
		triangle.append(lst[j:k+1])
		i += 1
		j = k+1
		k = j+i
	return triangle

def min_triangle_sum(n_elements):
	triangle = gen_triangle(list(lc_gen(n_elements)))
	
	sum_rows = []
	for row in triangle:
		rowsum = [0]
		for j in range(len(row)):
			rowsum.append(rowsum[j] + row[j])
		sum_rows.append(rowsum)
	
	res = 0
	for i in range(len(triangle)):
		for j in range(len(triangle[i])):
			curr_sum = 0
			for k in range(i, len(triangle)):
				curr_sum += sum_rows[k][k - i + 1 + j] - sum_rows[k][j]
				res = min(curr_sum, res)
	return res

'''
# Recursive approach, for around max 100 rows
def sub_triangles(lst):
	global res
	l = [i[1:] for i in lst if i[1:]]
	if(len(l) > 1):
		res = min(res, sum([sum(i) for i in l]))
		sub_triangles(l)
	
	l = [i[:-1] for i in lst if i[:-1]]
	if(len(l) > 1):
		res = min(res, sum([sum(i) for i in l]))
		sub_triangles(l)
	
	l = [i for i in lst[:-1] if i]
	if(len(l) > 1):
		res = min(res, sum([sum(i) for i in l]))
		sub_triangles(l)
'''

if __name__ == '__main__':
	print('Result:', min_triangle_sum(500500))
