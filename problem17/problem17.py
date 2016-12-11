cases = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

def num_to_word(num):
	word = []
	while(num):
		if num in cases:
			word.insert(0, cases[num])
			break
		if num % 100 in cases:
			word.insert(0, cases[int(num%100)])
			num -= num % 100
			continue
		if not num % 100:
			word.insert(0, cases[int(num/100)])
			word.insert(1, 'hundred')
			word.insert(2, 'and')
			break
		word.insert(0, cases[int(num%10)])
		num -= num % 10
	return word

if __name__ == '__main__':
	numbers = list(map(num_to_word, range(1,1000))) + ['one', 'thousand']
	
	#cleanup 'and's	
	for i in numbers:
		if i[-1] == 'and': del i[-1]
	
	print('Result:', sum(map(lambda i: len(''.join(i)), numbers)))
