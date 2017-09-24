def ispandigital(s):
	if len(s) != 9: return False
	for i in range(1,10):
		if str(i) not in s:
			return False
	return True

def check_multiples(n):
	i, concat = 1, ''
	while(len(concat) < 10):
		concat += str(n * i)
		if ispandigital(concat):
			return int(concat)
		i += 1
	return 0

print('Result:', max(map(check_multiples, range(1,10**6,2))))
