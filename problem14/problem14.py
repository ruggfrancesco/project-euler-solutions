def chain(n):
	chain_lenght = 1
	while n != 1:
		if not n % 2:
			n /= 2
		else:
			n = n*3 + 1
		chain_lenght += 1
	return chain_lenght

if __name__ == '__main__':
	max_chain_lenght = 0
	for i in range(1, 1000000):
		current_chain = chain(i)
		if current_chain > max_chain_lenght:
			max_chain_lenght = current_chain
			max_number_chain = i
	print('Result:', max_number_chain)
