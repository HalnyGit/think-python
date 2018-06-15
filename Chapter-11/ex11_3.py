def print_hist(h):
	t = sorted(h.keys())
	for i in t:
		print i, h[i]


def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d


word = 'parrot'
hist = histogram(word)
print_hist(hist)

