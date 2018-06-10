def remove_duplicates(t):
	res = []
	for item in t:
		if item not in res:
			res.append(item)
	return res

	
t1 = [1, 2, 3, 6, 2, 3, 4]
print remove_duplicates(t1)
			
	