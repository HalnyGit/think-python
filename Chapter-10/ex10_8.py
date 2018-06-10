
def has_duplicates(t):
	for elem in t:
		if t.count(elem) > 1:
			return True
	return False


t1 = [1, 'abc', 'cba', 3]
t2 = [1, 2, [1, 2]]
t3 = [1, 2, 1]
print 'has list t1 duplicates: ', has_duplicates(t1)
print 'has list t2 duplicates: ', has_duplicates(t2)
print 'has list t3 duplicates: ', has_duplicates(t3)
			
