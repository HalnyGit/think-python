def read_book_words(infile):
	"""Creates the list of words from the txt file (book)
	infile: text file
	return: list
	"""	
	import string
	
	fin = open(infile)
	lines = fin.readlines()
	
	words = []
	for line in lines[25:]: #skipping over the header information
		line = line.replace('-', ' ')
		t = line.split()
		for word in t:
			word = word.strip(string.punctuation + string.whitespace + '"')
			word = word.lower()
			words.append(word)
	words.remove('')
	return words
	
def read_list_words(infile):
	"""Creates the list of words from the text file where each word is in different line
	"""
	words = []
	fin = open(infile)
	for line in fin:
		words.append(line.strip())
	return words

def compare_book_dict(book_words, list_words):
	"""Checks which words from the book are not in the list of words
	book_words: words from the book
	dict_words: words from the word list
	return: set of the words in the book that are not in the word list
	"""
	set_book_words = set(book_words)
	set_list_words = set(list_words)
	return set_book_words.difference(set_list_words)
	
	
bw = read_book_words('emma.txt')
lw = read_list_words('words.txt')
print compare_book_dict(bw, lw)


	
	