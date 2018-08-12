def most_frequent(input_file):
	"""Takes a string and print the letters in decreasing order of frequency
	
	input_file - file with a text
	return - list of letters in decreasing order of frquency
	"""

	hist = dict()
	letters = []
	#convert text file into string
	s = open(input_file).read()
	
	#creates histogram of letters
	for letter in s:
		hist[letter] = hist.get(letter, 0) + 1
	
	#creates list of pairs (freq, letters) in sorted order
	for letter, freq in hist.iteritems():
		letters.append((freq, letter))
		letters.sort(reverse = True)
	
	res  =[]
	for freq, letter in letters:
		res.append(letter)
	
	return res
	
	
	
	
	
			
		

	

	
in_file = 'test.txt'
most_frequent(in_file)

