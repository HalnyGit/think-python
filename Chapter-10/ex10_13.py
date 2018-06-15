import bisect


def interlock_words(t):
	"""Print interlocked words from the list
		
		t: SORTED list
		
		return: list of interlock words
	"""
	for elem in t:
		if  bisearch(t, elem[0::2]) is not False: # do not write: "if bisearch(...):" becuse it will return False for index equal 0
			if bisearch(t, elem[1::2]) is not False:
				print elem, elem[0::2], elem[1::2]


def bisearch(t, word):
	"""Looks for element in the list using built-in bisect module
		
		t: sorted list
		word: searched element
		
		return: (index of element in the list or False)
	"""
	index = bisect.bisect_left(t, word)
	
	if index != len(t) and t[index] == word:
		return index
	else:
		return False

		
def read_words(input_file):
	t = []
	fin = open(input_file)
	for line in fin:
		t.append(line.strip())
	return t


t1 = read_words('words.txt')
interlock_words(t1)

