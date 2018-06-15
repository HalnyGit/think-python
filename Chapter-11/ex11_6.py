import time

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		a = fibonacci(n-1)
		b = fibonacci(n-2)
	return a + b

	
known = {0:0, 1:1}

def memo_fibonacci(n):
	if n in known:
		return known[n]
	res = fibonacci(n-1) + fibonacci(n-2)
	known[n] = res
	return res


def time_fibonacci(n):
	t0 = time.clock()
	result = fibonacci(n)
	return result, time.clock()

def time_memo_fibonacci(n):
	t0 = time.clock()
	result = memo_fibonacci(n)
	return result, time.clock()	
	
	
print 'memo:', time_memo_fibonacci(30)
print 'fibo:', time_fibonacci(30)
