from datetime import *

def print_day_of_week():
	"""Prints todays date of week"""
	d = date.today()
	print datetime.strftime(d, '%A')


def next_birthday():
	"""Calculate and prints your age and time to next birthday"""
	today = date.today()
	now = datetime.now()
	bday = int(raw_input('Enter the day of your birth (as integer)'))
	bmonth = int(raw_input('Enter the month of your birth ( as integer )'))
	byear = int(raw_input('Enter the year of your birth (as integer)'))

	birthday = date(byear, bmonth, bday)
	age = today -  birthday
	
	next_birthday = datetime(today.year, bmonth, bday, 0, 0, 0,)
	if next_birthday < now:
		next_birthday = next_birthday.replace(year = today.year + 1)
	time_to_birthday = next_birthday - now
	
	print 'You are {0:d} years old'.format(age.days/365)
	print 'Time to your next birthday: ', str(time_to_birthday).split('.')[0]



def double_day(n=2):
	"""Find the day when one born on date1 is n-times older (in days) then one born on date 2
	Note for n > 2 may not find solution within range
	"""
	date1 = date(1975, 9, 28)
	date2 = date(2014, 4, 9)
	ddate = date2 + timedelta(days = 1)
	x = ddate - date1
	y = ddate - date2
	print ddate, x, y
	while abs(n * y) != abs(x):
		ddate = ddate + timedelta(days = 1)
		x = ddate - date1
		y = ddate - date2
		print ddate, x, y
	print 'Your {0:d}-fold date is {1:}.'.format(n, ddate), 'One wil  be {0:d} and the other {1:d} years old.'.format(x.days/365, y.days/365)
			
print_day_of_week()
next_birthday()			
double_day(3)

# def n_fold(n=2):
	# """Test of double_day function on integers"""
	# x = 14074
	# y = 1
	# while n * y != x:
		# x += 1
		# y += 1
		# print x, y
	# print x, y
