from bisect import bisect_left
from time import clock
from random import shuffle


def bisearch(t, word):
	'''Looks for element in the list using bisection search
		
		t: sorted list
		word: searched element
		
		return: (run time, index of element in the list or False)
	'''
	t0 = clock()
	min = 0
	max = len(t) - 1
	while True:
		if word < t[min] or word > t[max]:
			return (clock(), False)
		elif word < t[(max + min) / 2]:
			max = (max + min) / 2
		elif word > t[(max + min) / 2]:
			min = ((max + min) / 2) + 1
		elif word == t[(max + min) / 2]:
			return (clock(), (max + min) / 2)
		
def read_words(input_file):
	t = []
	fin = open(input_file)
	for line in fin:
		t.append(line.strip())
	return t

def bisearch_2(t, word):
	'''Looks for element in the list using built-in bisect module
		
		t: sorted list
		word: searched element
		
		return: (run time, index of element in the list or False)
	'''
	t0 = clock()
	index = bisect_left(t, word)
	if index == len(t) or word != t[index]:
		return (clock(), False)
	return (clock(), index)

t1 = read_words('words.txt')
shuffle(t1)
word = 'zymurgy' 
print 'bisect:', bisearch(t1, word)
print 'bisect_2:', bisearch_2(t1, word)


