keyCube = lambda n: ''.join(sorted(str(n)))

if __name__=='__main__':	
	cubeDict = {1:[]}
	n, key = 2, 1
	
	while(len(cubeDict[key]) < 5):
		cube, n = n**3, n+1
		key = keyCube(cube)
		
		if key not in cubeDict: cubeDict[key] = []
		cubeDict[key].append(cube)

	print("Result:", cubeDict[key][0])
