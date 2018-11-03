from collections import Counter
import matplotlib.pyplot as plt
from itertools import combinations
from sys import exit
from tqdm import tqdm

def heatmap(l):
	plt.figure()
	plt.imshow(l)
	plt.colorbar()
	plt.show()

def isprime(n):
	if n==2: return True
	if not n%2: return False
	for i in range(3, int(n**.5+1), 2):
		if not n%i: return False
	return True

def hamming(a, b):
	a, b = str(a), str(b)
	tmp = [ i==j for i,j in zip(a,b) ]
	f_indexes = [i for i,v in enumerate(tmp) if not v]

	ispattern = True
	for i1, i2 in combinations(f_indexes, 2):
		if a[i1] != a[i2]: ispattern = False
		if b[i1] != b[i2]: ispattern = False

	return ''.join(map(str,f_indexes)) + '_' + str(ispattern)


primes = list(filter(isprime, range(int(10**5)+1, int(4*10**5), 2)) )

matrix_hamming = []
for p1 in tqdm(primes):
	ret = [hamming(p1, p2) for p2 in primes]
	matrix_hamming.append( ret )

common_counts = []
for irow, row in tqdm(enumerate(matrix_hamming)):
	row_true_cnt = Counter(filter(lambda m: 'True' in m, row))
	mc = row_true_cnt.most_common(1)[0]
	common_counts.append([irow, mc])

commonest = sorted(common_counts, key= lambda r: r[1][1], reverse=True)[0]

c_row = matrix_hamming[commonest[0]]
p_indexes = [i for i,v in enumerate(c_row) if v == commonest[1][0]]
prime_found = [primes[p] for p in p_indexes]

print(prime_found)
print('Result:', min(prime_found))