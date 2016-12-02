import functools

nums = filter(lambda x: not x%3 or not x%5, range(1000))
print(functools.reduce(sum, nums))
