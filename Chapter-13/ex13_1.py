def read_words(infile):
	
	import string
	punctu = string.punctuation
	
	fin = open(infile)
	lines = fin.readlines()
	words = []
	for line in lines:
		t = line.split()
		for word in t:
			clean_word = word.strip(punctu).lower()
			words.append(clean_word)
	return words


		
		
		


print read_words('test.txt')

