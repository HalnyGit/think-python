def is_sorted(t):
	for i in range(0, len(t)-1):
		if t[i] <= t[i+1]:
			flag = True 
		else:
			return False
	return flag

t1 = [1, 2, 3, 4]
t2 = [1, 2, 4, 3]

print 'is sorted t1: ', is_sorted(t1)
print 'is sorted t2: ', is_sorted(t2)