import time

def read_words(input_file):
	t0 = time.clock()
	t = []
	fin = open(input_file)
	lines = fin.readlines()
	for line in lines:
		t.append(line.strip())
	print 'read_words time:',time.clock()
	return t
	

def read_words_2(input_file):
	t0 = time.clock()
	t = []
	fin = open(input_file)
	lines = fin.readlines()
	for line in lines:
		t = t + [line.strip()]
	print 'read_words_2 time:', time.clock()	
	return t

		
read_words('words.txt')
read_words_2('words.txt')

	