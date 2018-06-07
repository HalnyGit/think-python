def capitalize_all(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res

def capitalize_nested(t):
	res = []
	for item in t:
		if isinstance(item, list):
			res.append(capitalize_all(item))
		else:
			res.append(item)
	return res
	
t1 = [['benio', 'filutek'], 'y', ['summer', 'time', 'joy']]

print capitalize_nested(t1)

