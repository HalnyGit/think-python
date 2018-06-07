def is_palindrome(son, mom):
	mom = str(mom)
	son = str(son).zfill(len(mom))
	return son == mom[::-1]

def check_pali(delta = 10):
	while delta < 70:
		
		son = 0
		mom = son + delta
		counter = 1
		while mom <= 120 and counter <= 8:
			if is_palindrome(son, mom):
				
				if counter == 8:
					delta = mom - son
					print 'delta: {:d}'.format(delta)
					final_result(delta)	
				
				counter += 1
			son += 1
			mom += 1
		
		delta += 1

def final_result(delta):
	son = 0
	mom = son + delta
	counter = 1
	while mom <= 120 and counter <= 8:
		if is_palindrome(son, mom):
			print 'counter: {0:2d}, son: {1:2d}, mom: {2:2d}'.format(counter, son, mom)
			counter += 1
		son += 1
		mom += 1
	check_pali(delta + 1)
		
check_pali()