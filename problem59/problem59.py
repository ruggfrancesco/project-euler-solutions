def mostfreq(t):
	d = dict()
	for i in t:
		d[i] = 1 if i not in d else d[i]+1
	return max(d, key=lambda x: d[x])



if __name__ == '__main__':
	text = open('cipher.txt', 'r').read().strip().split(',')
	text = list(map(int, text))
	
	mf = mostfreq(text)
	
	#I assumed the key analysing the text.
	#1: space is the most common character. In the second column it returns valid ascii chars.
	#2: the second letter is a 't', the fourth is a space. I assume the word is 'the'.
	#I got the key 'god'
	
	key = [2 ^ ord('e'), mf ^ ord(' '), 12 ^ ord('h')]
	
	res = 0
	for i in range(0, len(text), 3):
		for j in range(len(text[i:i+3])):
			res += text[i+j] ^ key[j]
	
	print('Result:', res)
