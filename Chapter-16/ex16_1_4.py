class Time(object):
	"""Represents the time of day.
	attributes: hour, minute, second
	"""

def print_time(t):
	print '{0:02d}:{1:02d}:{2:02d}'.format(t.hour, t.minute, t.second)

def is_after(t1, t2):
	"""Checks if time1 follows time2.
	t1, t2: Time objects
	return: Boolean
	"""
	t1_seconds = t1.hour * 3600 + t1.minute * 60 + t1.second
	t2_seconds = t2.hour * 3600 + t2.minute * 60 + t2.second
	return t1_seconds > t2_seconds

def add_time_bug(t1, t2):
	"""(This is an exercise only - function does not work correctly for seconds, minutes > 60)
	Add times of 2 time objects
	"""
	sum = Time()
	sum.hour = t1.hour + t2.hour
	sum.minute = t1.minute + t2.minute
	sum.second = t1.second + t2.second
	return sum
	
def add_time(t1, t2):
	sum = Time()
	total = time_to_int(t1) + time_to_int(t2)
	return int_to_time(total)

def increment(time, seconds):
	"""(Modifier - modifies parameters of an object)
	Increment the time object by modifying its parameters
	"""
	time.second += seconds
	q = divmod(time.second, 60)
	time.second = q[1]
	time.minute += q[0]
	q = divmod(time.minute, 60)
	time.minute = q[1]
	time.hour += q[0]
	
def new_time_incremented(primary_time, seconds):
	"""(Pure function - creates and returns new object)
	Creates a new time object based on incrementing primary time by seconds
	"""
	new_time = Time()
	new_time.second = primary_time.second
	new_time.minute = primary_time.minute
	new_time.hour = primary_time.hour
	
	new_time.second += seconds
	q = divmod(new_time.second, 60)
	new_time.second = q[1]
	new_time.minute += q[0]
	q = divmod(new_time.minute, 60)
	new_time.minute = q[1]
	new_time.hour += q[0]
	return new_time
	
def time_to_int(time):
	seconds = (time.hour * 60**2) + (time.minute * 60**1) + (time.second * 60**0)
	return seconds
	
def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time1 = Time()
time1.hour = 9
time1.minute = 45
time1.second = 0

time2 = Time()
time2.hour = 1
time2.minute = 35
time2.second = 0

print 'does time1 follow time2:',	
print is_after(time1, time2)

done = add_time_bug(time1, time2)
print 'add_time_bug:',
print_time(done)

done = add_time(time1, time2)
print 'add_time:',
print_time(done)

increment(time1, 3673)
print 'modifier - time incremented:',
print_time(time1)

new_time = new_time_incremented(time1, 3673)
print 'pure function - new time object:',
print_time(new_time)
