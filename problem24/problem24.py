from itertools import permutations

print('Result:', ''.join(map(lambda d: str(d), list(permutations(range(10)))[10**6-1])))
