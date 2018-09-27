"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""


def make_word_dict():
	"""Reads file and returns dictonary with words as keys and values
	""" 
	d = dict()
	fin = open('test.txt')
	for line in fin:
		word = line.strip().lower()
		d[word] = word
	
	for letter in('a', 'i', ''):
		d[letter] = letter
	return d


"""Dictonary that stores reducible words with its reducible children
"""
memo = dict()
memo[''] = ['']


def children(word, word_dict):
	"""Returns a list of all words that can be formed by removing one letter.
	word: string
	return: list of children
	"""
	res = []
	for i in range(len(word)):
		letters = list(word)
		letters.pop(i)
		child = "".join(letters)
		if child in word_dict:
			res.append(child)
	return res


def is_reducible(word, word_dict):
	"""If word is reducible, returns a list of its reducible children.
	Also adds an entry to the memo dictionary.
	A string is reducible if it has at least one child that is 
	reducible.  The empty string is also reducible.

	word: string
	word_dict: dictionary with words as keys
	"""
	if word in memo:
		return memo[word]
	
	# check each of the children and make a list of the reducible ones
	res=[]
	for child in children(word, word_dict):
		t = is_reducible(child, word_dict)
		if t:
			res.append(child)
	
	# memorize and return the result
	memo[word] = res
	return res
	
		
def reducible_only(word_dict):
	"""Checks all words in the word_dict; returns a list of reducible ones.
	word_dict: dictionary with words as keys
	Creates the list of reducible words only
	"""
	res = []
	for word in word_dict:
		t = is_reducible(word, word_dict)
		if t != []:
			res.append(word)
	return res


def print_trail(word):
	"""Prints the sequence of words that reduces this word to the empty string.
	If there is more than one choice, it chooses the first.
	word: string
	"""
	if len(word) == 0:
		return
	print word,
	t = is_reducible(word, word_dict)
	print_trail(t[0])

	
def print_longest_words(word_dict):
	words = reducible_only(word_dict)
	
	# use DSU to sort by word length
	t = []
	for word in words:
		t.append((len(word), word))
	t.sort(reverse = True)
	
	# print the longest 5 words
	for length, word in t[0:5]:
		print_trail(word)
		print '\n'
		
	
word_dict = make_word_dict()
print_longest_words(word_dict)


