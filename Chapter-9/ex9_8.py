def odometer(start = '000000'):
	while int(start) <= 999999:
		last_four = start[2:]
		if is_palindrome(last_four, last_four):
			s_int = int(start) + 1
			last_five = str(s_int)[1:]
			if is_palindrome(last_five, last_five):
				s_int += 1
				s = str(s_int).zfill(6)
				mid_four = s[1:-1]
				if is_palindrome(mid_four, mid_four):
					s_int += 1
					s = str(s_int).zfill(6)
					if is_palindrome(s, s):
						print 'odometer reading: ', start
						start = str(int(start) + 1).zfill(6)
					else:
						start = str(int(start) + 1).zfill(6)
				else:
					start = str(int(start) + 1).zfill(6)
			else:
				start = str(int(start) + 1).zfill(6)
		else:
			start = str(int(start) + 1).zfill(6)

		
def is_palindrome(word1, word2):
    if word1 == word2[::-1]:
        return True
    else:
        return False
		

odometer()
