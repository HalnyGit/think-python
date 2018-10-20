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

def make_anagrams_map(map_of_codes):
	"""Returns map of anagrams where key is its unique letter code
	and values are list of anagrams
	
	map_of_codes - dictonary that maps each word to its letter code
	return - dictonary {letter_code:[anagram1, anagram2,...]}
	"""
	#creates a dictonary that maps single letter code to all possible anagrams
	map_of_anagrams = dict()
	for word, code in map_of_codes.iteritems():
		map_of_anagrams.setdefault(code, []).append(word)
	return map_of_anagrams
				


