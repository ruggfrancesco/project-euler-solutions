#All credits to:
#https://pypi.python.org/pypi/roman

from functools import reduce

romanNumeralMap = (('M',  1000), ('CM', 900), ('D',  500), ('CD', 400),
                   ('C',  100), ('XC', 90), ('L',  50), ('XL', 40),
                   ('X',  10), ('IX', 9), ('V',  5), ('IV', 4), ('I',  1))

def toRoman(n):
	result = ""
	for numeral, integer in romanNumeralMap:
		while n >= integer:
			result += numeral
			n -= integer
	return result

def fromRoman(s):
    result, index = 0, 0
    for numeral, integer in romanNumeralMap:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result

if __name__ == '__main__':
	print('Result:', sum([len(n)-len(toRoman(fromRoman(n))) for n in open('p089_roman.txt', 'r').read().strip().split('\n')]))
