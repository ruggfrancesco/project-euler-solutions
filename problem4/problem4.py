from sys import exit

'''
#I was just a kid when I wrote this. :P
def ispalindrome(obj):
	l = len(obj)-1
	for i in range(0, l):
		if obj[i] != obj[l-i]: return False
	return True
'''

ispalindrome = lambda obj: obj==obj[::-1]

if __name__ == '__main__':
	print('Result:', max([n*m for n in range(999, 100, -1) for m in range(n, 100, -1) if ispalindrome(str(n*m))]))
