def build_dict(input_file):
	"""Reads from a file and builds a dictionary that maps from
	each word to a string that represents its pronuciation.
	
	input_file: file
	returns: map from word to its pronunciationwor
	"""
	t = []
	pronuciation_dict = dict()
	fin = open(input_file)
	
	for line in fin:
		#skip over the comments
		if line[0] == '#': continue
		t.append(line.strip().split('  '))

	for elem in t:
		if len(elem) > 1:
			pronuciation_dict[elem[0]] = elem[1]
	
	return pronuciation_dict


def is_homophone(word1, word2, pron_dict):
	"""Chcecks if two words are homophones"
	word1 - first word
	word2 - second word
	pron_dict - dictonary that maps strings/words to a string that represents its pronuciation
	returns: True if two words are homophones or False if they are not
	"""
	
	if pron_dict[word1] == pron_dict[word2]:
		return True
	return False
	

def get_homophones(pron_dict):
	"""Looks for homophone words with the following property:
	When you remove the first letter, the remaining letters form a homophone of the original word, that is a word
	that sounds exactly the same. Replace the first letter, that is, put it back and remove
	the second letter and the result is yet another homophone of the original word.
	
	d = dictionary that maps words to its pronuciation
	returns: list of homophones
	"""
	t = []
	for word in pron_dict:
		word2 = word[1:]
		word3 = word[0] + word[2:]
		check1 = False
		check2 = False
		if word2 in pron_dict:
			check1 = is_homophone(word, word2, pron_dict)
		if check1 == True and word3 in pron_dict:
			check2 = is_homophone(word, word3, pron_dict)
		if check2:
			t.append(word)
	
	return t

	
infile = 'c06d.txt'
pron_dictonary = build_dict(infile)
print get_homophones(pron_dictonary)
		
			
		
			
			

					
					
