def read_words(input_file):
	"""Reads file and returns list of words
	""" 
	words = []
	fin = open(input_file)
	for line in fin:
		words.append(line.strip())
	return words

def make_children(words):
	"""Create dictonary that maps words(keys) to its children, 
	where child is a word formed by removing one letter from it's parent
	
	words - list of words
	return - dictonary: parent -> children
	"""
	children = dict()
	for word in words:
		if len(word) == 1:
			children.setdefault(word, [])
		if len(word) > 1:
			for i in range(len(word)):
				letters = list(word)
				letters.pop(i)
				child = "".join(letters)
				if child in words:
					if child not in children.get(word, 'Nothing'):
						children.setdefault(word, []).append(child)
	return children

# def make_branch(children):
	# branch = []
	# for parent, child in children.iteritems():
		
		
	
words = read_words('test.txt')
print make_children(words)

	


		
		
	