def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d


word = 'salamandra'
print histogram(word)