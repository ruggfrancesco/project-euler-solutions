ispalindrome = lambda s: s == s[::-1]

def islychrel(num):
	for cnt in range(50):
		num = str(int(num) + int(str(num)[::-1]))
		if ispalindrome(num):
			return False
	return True

if __name__ == '__main__':
	print('Result:', len(list(filter(lambda x: x, map(lambda n: islychrel(n), range(1,10000))))))
