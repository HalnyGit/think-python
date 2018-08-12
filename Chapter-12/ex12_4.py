#1 & 2
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

def sets_of_anagrams(map_of_codes, n):
	"""Returns sets of anagrams sorted in descending order in respect to the size of sets
	
	map_of_codes - dictonary that maps each word to its letter code
	n - integer that represents minimum size of set
	return - list that contains sets of anagrams in respect to their size
	"""
	#creates a dictonary that maps single letter code to all possible anagrams
	map_of_anagrams = dict()
	for word, code in map_of_codes.iteritems():
		map_of_anagrams.setdefault(code, []).append(word)
	#creates a sorted list with sets of anagrams and its size, in descending order in respect to size of set
	set_sizes = []
	for code, anagrams in map_of_anagrams.iteritems():
		set_sizes.append((len(anagrams), anagrams))
	set_sizes.sort(reverse = True)
	#creates a sorted list with sets of anagrams
	sets_of_anagrams = []
	for lenght, anagrams in set_sizes:
		if lenght >= n:
			sets_of_anagrams.append(anagrams)
	return sets_of_anagrams
				
	
words = read_words('words.txt')
d = map_of_codes(words)
res = sets_of_anagrams(d, 2)
# for elem in res:
	# print elem

#3
def bingo(sets_of_anagrams, k):
	"""Returns largest sets of anagrams in respect to the number of letters in the anagrams
	
	sets_of_anagrams - list that contains sets of anagrams
	k - integer that represents number of letters in anagram
	return - list
	"""
	#creates list with sets of k-length anagrams
	k_length_anagrams = []
	for anagrams in sets_of_anagrams:
		if len(anagrams[0]) == k:
			k_length_anagrams.append(anagrams)
	#looking for set with largest number of anagrams
	sizes_of_sets = []
	for anagrams in k_length_anagrams:
		sizes_of_sets.append(len(anagrams))
	largest = max(sizes_of_sets)
	#creates a list with sets of largest number of anagrams only
	bingo = []
	for anagrams in k_length_anagrams:
		if len(anagrams) == largest:
			bingo.append(anagrams)
	return bingo
		
scrabble = bingo(res, 8)
for elem in scrabble:
		print elem

