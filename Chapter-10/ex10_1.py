def nested_sum(t):
	"""Takes the nested list of integers and add update
		the elements from all of the nested list
		
		t - list with nested list containing integers or floats
		return - sum of all nested list
	"""
	collector = 0
	for item in t:
		collector += sum(item)
	return collector

	
t1 = [[10, 7, 13], [-10], [4, 8, 6], []]

print nested_sum(t1)