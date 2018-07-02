def has_duplicates(t):
	"""Checks if any element appears more than once in sequence.
	
	t: sequence
	"""
	d = {}
	for x in t:
		if x in d:
			return True
		d[x] = True
	return False

word = 'drumm'
print has_duplicates(word)
