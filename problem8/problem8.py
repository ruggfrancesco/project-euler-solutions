from functools import reduce

number = open('number', 'r').read().strip()
treshold = 13

result = max([reduce(lambda x,y: int(x)*int(y), [d for d in number[i:i+treshold]]) for i in range(0, len(number)-(treshold-1))])

print('Result:', result)
