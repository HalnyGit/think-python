h = {'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1 }

def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse


def mod_invert_dict(d):
	inverse = dict()
	for key, val in d.iteritems():
		inverse.setdefault(val, []).append(key)
	return inverse


print invert_dict(h)
print mod_invert_dict(h)




