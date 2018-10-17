import matplotlib.pyplot as plt
import numpy as np
import random
import string
import math


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

def rank_words(word_num_map):
	t = []
	for word, num in word_num_map.iteritems():
		t.append((num, word))
	t.sort(reverse = True)
	
	rank_dict = dict()
	rank = 0
	for num, word in t:
		rank += 1
		rank_dict[word] = (rank, num)
	return rank_dict
	

def create_plot(rank_dict):
	log_f = []
	log_r = []
	for rank, num in rank_dict.values():
		log_f.append(math.log(num))
		log_r.append(math.log(rank))

	x = log_r
	y = log_f
	
	plt.title('Zipf plot')
	plt.xlabel('rank')
	plt.ylabel('frequency')
	plt.plot(x, y)
	plt.show()
		
book_words = read_book_words('emma.txt')
word_num_map = make_word_num_map(book_words)
rank_dict = rank_words(word_num_map)
create_plot(rank_dict)

	
		