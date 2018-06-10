import bisect


def reverse_pairs(t):
	"""Returns pairs of reversed words from the list
		
		t: sorted list
		
		return: list of reverse pairs
	"""
	res = []
	
	gen = (elem for elem in t if len(elem) != 3)
	
	for elem in gen:
		reversed = elem[::-1]
		rev_index = bisearch(t, reversed)
		
		if rev_index:
			new_pair = sorted([elem, t[rev_index]])
			
			if new_pair not in res:
				res.append(new_pair)
	
	return [res, len(res)]

	
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
print reverse_pairs(t1)

