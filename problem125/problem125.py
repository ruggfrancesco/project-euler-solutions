ispalindrome = lambda obj: obj==obj[::-1]

if __name__ == '__main__':
	res = []
	n = 10**8
	limit = int(n**.5)+1

	for i in range(1, limit):
		candidate = i**2
		for j in range(i+1, limit):
			candidate += j**2
			if candidate <= n:
				if ispalindrome(str(candidate)):
					res.append(candidate)
			else:
				break
	print('Result:', sum(set(res)))
