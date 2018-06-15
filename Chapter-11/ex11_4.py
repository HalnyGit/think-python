h = {'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1 }


def reverse_lookup(d, v):
	for k in d:
		if d[k] == v:
			return k
	raise ValueError('value does not appear in the dictionary')


def mod_reverse_lookup(d, v):
	t = []
	for k in d:
		if d[k] == v:
			t.append(k)
	return sorted(t)

	
#print reverse_lookup(h, 3)
print mod_reverse_lookup(h, 1)

