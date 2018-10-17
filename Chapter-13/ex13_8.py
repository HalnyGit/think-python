import random
import string

def read_book_words(infile):
	"""Creates the list of words from the txt file (book)
	infile: text file
	return: list
	"""	
	fin = open(infile) 
	lines = fin.readlines()
	words = []
	for line in lines[25:16263]: #skipping over the header information
		line = line.replace('-', ' ')
		t = line.split()
		for word in t:
			word = word.strip(string.punctuation + string.whitespace + '\xe2\x80\x9c' + '\xe2\x80\x9d')
			word = word.lower()
			words.append(word)
	#words.remove('')
	return words

	
def make_word_num_map(words):
	"""Creates dictonary that maps words to number of occurance in the text
	words: list of words
	return: dictonary {word:number of occurrence}
	"""
	word_num_map = dict()
	for word in words:
		word_num_map[word] = word_num_map.get(word, 0) + 1
	return word_num_map


def make_freq_word_map(histogram):
	"""Creates dictonary that maps integer to the specific word
	the integer represent proportion of word occurence in the text
	d: dictonary (histogram) that matches letter to number of occurance
	return: dictonary {proportion:word}
	"""
	freq_word_map = dict()
	collector = 0		
	#creating dictonary with proportion as keys and word as values
	for word, num in histogram.iteritems():
		collector = collector + num
		freq_word_map[collector] = freq_word_map.get(collector, word)
	return freq_word_map


def choose_random_word(freq_word_map):
	"""Choose a random word with probability equal to
	proportion of occureance
	"""
	#finding integer that matches the exact key-proportion
	total_words = max(freq_word_map.keys())
	pick = random.randint(1, total_words)
	while pick not in freq_word_map.keys():
		pick = pick + 1
	return freq_word_map[pick]

	
def make_prefix_suffix_map(words):
	"""Creates dictonary that maps word (prefix) to is suffixes
	words: list of words in order of its appearance
	return: dictonary {prefix:[sufix1, suffix2,...]}
	"""
	prefix_suffix_map = dict()
	for i in range(len(words)-1):
		prefix = words[i]
		suffix = words[i + 1]
		prefix_suffix_map.setdefault(prefix, []).append(suffix)
	for prefix in prefix_suffix_map:
		unique_suffix_list = list(set(prefix_suffix_map[prefix]))
		prefix_suffix_map[prefix] = unique_suffix_list
	return prefix_suffix_map
	
	
book_words = read_book_words('emma.txt')
word_num_map = make_word_num_map(book_words)
freq_word_map = make_freq_word_map(word_num_map)
random_word = choose_random_word(freq_word_map)
prefix_suffix_map = make_prefix_suffix_map(book_words)


def make_random_text(prefix, n=500):
	#prefix = random_word
	for i in range(n):
		print prefix,
		if prefix not in prefix_suffix_map:
			prefix = random_word
		suffix = random.choice(prefix_suffix_map[prefix])
		prefix = suffix
		i += 1

make_random_text(random_word)


	



	
	

	



