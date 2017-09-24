palindrome = lambda n: n==n[::-1]

print('Result:', sum(filter(lambda n: palindrome(str(n)) and palindrome(str(bin(n))[2:]), range(1,10**6,2))))
