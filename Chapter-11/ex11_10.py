def rotate_word(word, n):
    """Rotate a letter in a word by n places within alphabet and creates new, 'rotated' word.

    word: string
    n: integer

    Returns: string ('rotated' word)
    """

    word = word.lower()
    rotated_word = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in word:
        index = alphabet.find(letter)
        index = (index + n) % 26
        rotated_word = rotated_word + alphabet[index]
    return rotated_word

def read_words_dict(input_file):
	"""Reads file of words and creates dictionary with words as keys
	
	input_file: text file with words

	Returns: dictionary
	"""
	d = dict()
	n = 0
	fin = open(input_file)
	for line in fin:
		d[(line.strip())] = n
		n += 1
	return d

worddict = read_words_dict('words.txt')

def pairs_of_rotated_words(wd, n):
	"""Looks for possible pairs of rotated words
	
	wd: dictionary of words (words as keys)
	n: integer - rotator
	
	Returns: dictionary of rotated words pairs
	"""
	rwd = dict()
	for k in wd:
		rotated_word = rotate_word(k, n)
		if rotated_word in wd:
			rwd[k] = rotated_word
	return rwd
			
print pairs_of_rotated_words(worddict, 3)
	