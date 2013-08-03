f = open('lastn.txt')
lines = f.readlines()
for line in lines:
	tempLine = line.split('\t')
	print (tempLine[0])
