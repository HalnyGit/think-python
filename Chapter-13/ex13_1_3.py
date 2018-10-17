def read_words(infile):
	"""Creates the list of words from the txt file
	infile: text file
	return: list
	"""	
	import string
	p = string.punctuation
	
	fin = open(infile)
	lines = fin.readlines()
	words = []
	for line in lines[25:]: #skipping over the header information
		t = line.split()
		for word in t:
			clean_word = word.strip(p).lower()
			words.append(clean_word)
	words.remove('')
	return words

def make_word_dict(words):
	"""Creates dictonary of string from the word list with words as keys
	and print the number of times the words has been used as values
	words: list of words
	return: dictonary {word:number of occurrence}
	"""
	word_dict = dict()
	for word in words:
		word_dict[word] = word_dict.get(word, 0) + 1
	return word_dict
	
def print_word_occur(word_dict, n):
	"""Print out n words with the highest number of occurrences in the text
	word_dict: dictonary {word:number of occurrence} 
	"""
	t = []
	for word, freq in word_dict.iteritems():
		t.append((freq, word))
	t.sort(reverse=True) #DSU to sort by number of word occurrence	
	for freq, word in t[:n]:
		print word, freq
	

words = read_words('dracula.txt')
wd = make_word_dict(words)
print_word_occur(wd, 100)
