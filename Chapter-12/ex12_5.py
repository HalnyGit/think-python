# def is_anagram(word1, word2):
	# """Checks if 2 words are anagrams and if so it returns True
	# """
	# return sorted(word1) == sorted(word2)

def read_words(input_file):
	"""Reads file and returns list of words
	""" 
	words = []
	fin = open(input_file)
	for line in fin:
		words.append(line.strip())
	return words

def letter_code(word):
	"""Sorts the letters in the word to create its code of letters
	
	word - string, word
	return - string of sorted letters of the word
	"""
	return ''.join(sorted(word))

def map_of_codes(words):
	"""Returns dictonary that maps each word to its letter code
	
	words - list of words
	return - dictonary
	"""
	map_of_codes = dict()
	codes = []
	for word in words:
		map_of_codes[word] = letter_code(word)
	return map_of_codes

def sets_of_anagrams(map_of_codes):
	"""Returns sets of anagrams
	
	map_of_codes - dictonary that maps each word (key) to its letter code
	return - list that contains sets of anagrams
	"""
	#creates a dictonary that maps single letter code to all possible anagrams(words)
	map_of_anagrams = dict()
	for word, code in map_of_codes.iteritems():
		map_of_anagrams.setdefault(code, []).append(word)
	#creates a list with sets of anagrams
	sets_of_anagrams = []
	for code, anagrams in map_of_anagrams.iteritems():
		sets_of_anagrams.append(anagrams)
	return sets_of_anagrams

def methatesis_pairs(sets_of_anagrams):
	methatesis_pairs = []
	for set in sets_of_anagrams:
		for i in range(len(set)-1):
			for n in range(1, len(set)):
				if is_methatesis_pair(set[i], set[n]):
					methatesis_pairs.append((set[i], set[n]))
	return methatesis_pairs
			
def is_methatesis_pair(anagram1, anagram2):
	"""Returns True if two anagrams are "methatesis pair"
	(meaning: you can transform one into the other by swapping two letters
	eg.'converse' and 'conserve'
	"""
	counter = 0
	for i in range(len(anagram1)):
		if anagram1[i] != anagram2[i]:
			counter += 1
	if counter == 2:
		return True
	else:
		return False

words = read_words('words.txt')
d = map_of_codes(words)	
s = sets_of_anagrams(d)
mp = methatesis_pairs(s)
for pair in mp:
	print pair
	
			
	
	
	
	
	
	
	