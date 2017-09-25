# Did this in sixth grade.
# No idea of what this code does

d, s, r = 1, 1, 0

for i in range(-1,1001,2):
    d = d + s*4 + i*10
    s += i*4
    if r < d: r = d

print('Result:', r-4)
