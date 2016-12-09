if __name__ == '__main__':
	print('Result:', len([n**e for n in range(1,11) for e in range(25) if len(str(n**e))==e]))
