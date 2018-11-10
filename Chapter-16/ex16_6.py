class Time(object):
	"""Represents the time of day.
	attributes: hour, minute, second
	"""
	
def print_time(t):
	print '{0:02d}:{1:02d}:{2:02d}'.format(t.hour, t.minute, t.second)

def add_time(t1, t2):
	sum = Time()
	total = time_to_int(t1) + time_to_int(t2)
	return int_to_time(total)

def time_to_int(time):
	seconds = (time.hour * 60**2) + (time.minute * 60**1) + (time.second * 60**0)
	return seconds
	
def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time

def mul_time(time, number):
	"""Multiplicates time by number.
	return: time object
	"""
	new_time = Time()
	mul_int = time_to_int(time) * number
	new_time = int_to_time(int(round(mul_int)))	
	return new_time
	
def average_pace(finishing_time, distance):
	"""Calculates average pace in a race.
		finishing_time: time object
		distance: distance in km
		return: time object that represents average pace (time per km)
	"""
	av_pace = Time()
	av_pace = mul_time(finishing_time, 1.0/distance)
	return av_pace

time1 = Time()
time1.hour = 0
time1.minute = 59
time1.second = 30

time2 = mul_time(time1, 10)
time3 = average_pace(time2, 10)

print_time(time1)
print_time(time2)
print_time(time3)


