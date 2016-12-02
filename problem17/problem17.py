import re

cases = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
numbers = []

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
			word.insert(0, cases[int(num/100)])# + ' hundred')
			word.insert(1, 'hundred')
			word.insert(2, 'and')
			break
		word.insert(0, cases[int(num%10)])
		num -= num % 10
	numbers.append(word)
	return word

def lenght(k):
	cnt = 0
	for i in k:
		cnt += len(i)
	return cnt

if __name__ == '__main__':
	#create numbers list
	for i in range(1, 1000): num_to_word(i)
	numbers.append(['one', 'thousand'])
	
	#cleanup 'and's	
	for i in numbers:
		if i[-1] == 'and': del i[-1]
	
	#count number of letters
	count=0
	for i in range(0, len(numbers)):
		tmp = lenght(numbers[i])
		count += tmp
		print("Number: {0} = {1} - len->{2}".format(i+1, numbers[i], tmp))

	print("Total lenghts =", count)

'''
	#Attempts
	print("Number({0}) to words: {1}".format(1, num_to_word(1)))
	print("Number({0}) to words: {1}".format(12, num_to_word(12)))
	print("Number({0}) to words: {1}".format(145, num_to_word(145)))
	print("Number({0}) to words: {1}".format(300, num_to_word(300)))
	print("Number({0}) to words: {1}".format(312, num_to_word(312)))
	print("Number({0}) to words: {1}".format(555, num_to_word(555)))
	print("Number({0}) to words: {1}".format(411, num_to_word(411)))
	print("Number({0}) to words: {1}".format(768, num_to_word(768)))
	print("Number({0}) to words: {1}".format(999, num_to_word(999)))
'''
