def middle(t):
	return t[1:-1]

def chop(t):
	t.pop(0)
	t.pop(len(t)-1)
	return None

	
t1 = ['a', 'b', 'c', 'd']

new_list = middle(t1)
print 'new_list created by middle() function: ', new_list
print 't1 after middle(): ', t1


chop(t1)
print 't1 after chop(): ', t1



