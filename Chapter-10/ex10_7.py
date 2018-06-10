def is_anagram(word1, word2):
	return sorted(word1) == sorted(word2)


print is_anagram('abba', 'baba')
print is_anagram('hey', 'how')
print is_anagram('double', 'trouble')
print is_anagram('python', 'typhon')

