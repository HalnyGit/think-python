import shelve
from anagrams import *

words = read_words('words.txt')
anagrams_map = make_anagrams_map(map_of_codes(words))

def store_anagrams(map):
		d = shelve.open('anagrams.db', 'c')
		for key, values in anagrams_map.iteritems():
			d[key] = values
		d.close()
		
def read_anagrams(word, datafile):
		code = letter_code(word)
		d = shelve.open(datafile, 'r')
		try:
			print d[code]
		except:
			print 'This word has no anagrams'

store_anagrams(anagrams_map)
read_anagrams('sport', 'anagrams.db')


