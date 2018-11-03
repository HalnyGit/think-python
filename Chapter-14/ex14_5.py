def linecount(filename):
	count = 0
	for line in open(filename):
		count += 1
	return count

print linecount('ex14_5.py')
