import random


def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d


def choose_from_hist(d):
	"""Choose a letter from histogram with probability
	with proportion to frequency
	d: dictonary (histogram) that matches letter to number of occurance
	return: letter
	"""
	freq_dict = dict()
	collector = 0	
	
	#creating dictonary with proportion as keys and letter as values
	for letter, num in d.iteritems():
		collector = collector + num
		freq_dict[collector] = freq_dict.get(collector, letter)	
	
	#finding integer that matches the exact key-proportion
	all_letter_sum = sum(d.values())
	pick = random.randint(1, all_letter_sum)
	while pick not in freq_dict.keys():
		pick = pick + 1
	return freq_dict[pick]

	
word = 'abbccc'
hist = histogram(word)
print choose_from_hist(hist)

