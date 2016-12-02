nums = open('numbers', 'r').read().strip().split()

x = sum([int(i) for i in nums])

print('Result:', int((x-(x % 10**42))/10**42))
