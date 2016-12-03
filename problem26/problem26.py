def reminders(n):
	reminders = [1 % n]
	
	while((10*reminders[-1]) % n not in reminders):
		reminders.append((10*reminders[-1]) % n)
	
	return len(reminders)

if __name__ == '__main__':
	print('Result:', max(map(lambda n: (reminders(n), n), range(1, 1000)))[1])
