def read_dict(input_file):
	"""Reads from a file and builds a dictionary that maps from
	each word to astring that represents its pronuciation.
	
	input_file: file
	returns: map from word to its pronunciation
	"""
	t = []
	pronuciation_dict = dict()
	fin = open(input_file)
	
	for line in fin:
		#skip over the comments
		if line[0] == '#': continue
		
		t.append(line.strip().split('  '))
	
	for elem in t:
		pronuciation_dict[elem[0]] = elem[1]
	
	return pronuciation_dict
		
infile = 'htest.txt'
print read_dict(infile)

def get_homophones(d):
	"""Looks for homophones of five letter words with the following property:
	When you remove the first letter, the remaining letters form a homophone of the original word, that is a word
	that sounds exactly the same. Replace the first letter, that is, put it back and remove
	the second letter and the result is yet another homophone of the original word.
	
	d = dictionary that maps words to its pronuciation
	returns: homophones
	"""
	
	for k in d:
		#looks for 5 letter words
		if ')' in k: #includes words with secondary pronounciation
			n = len(k[:-3])
		else:
			n = len(k)
		
		#looks for 4 letter words after removing the first letter
		if n == 5:
			if ')' in k:
				four_letter_word = k[1:-3]
			else:
				four_letter_word = k[1:]
				
			if four_letter_word in d:
				if d[k] == d[four_letter_word]:
					next_word
					
					
					
