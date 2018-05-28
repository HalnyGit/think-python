from sys import argv

script, in_file = argv

def has_triple_pairs(word):
	""" checks if word has three consecutives pairs of letters"""
	counter = 0
	i = 0
	while i < len(word) - 1:
			if word[i] == word[i + 1]:
				counter += 1
				i += 2
				if counter == 3:
					return True
			else:
				counter = 0
				i += 1
	return False

def search_triple_pairs():
	fin = open(in_file)
	for line in fin:
		word = line.strip()
		if has_triple_pairs(word):
			print word

search_triple_pairs()

                                

                        
