def cumulative_sum(t):
	res = []
	for i in range(0, len(t)):
		res.append(sum(t[:i+1]))
	return res
	
t1 = [1, 3, 5]

print cumulative_sum(t1)
