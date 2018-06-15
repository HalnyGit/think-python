from time import clock
import bisect


def in_dict(d, k):
	""" Chcecks if key in dictionary
		
		d: dictionary
		k: key
		
		return: (True/False, run time)
	"""
	t0 = clock()
	return (k in d, clock())
	
		
def bisearch(t, word):
	"""Looks for element in the list using built-in bisect module
		
		t: sorted list
		word: searched element
		
		return: (index of element in the list or False)
	"""
	t0 = clock()
	index = bisect.bisect_left(t, word)
	
	if index != len(t) and t[index] == word:
		return (index, clock())
	else:
		return (False, clock())

		
def read_words(input_file):
	t = []
	fin = open(input_file)
	for line in fin:
		t.append(line.strip())
	return t

t1 = read_words('words.txt')
word = 'dupa'
wd = dict()
for elem in t1:
	wd[elem] = len(elem)
print 'dict: ', in_dict(wd, word)
print 'list: ', bisearch(t1, word)
	

