class Time(object):
	"""Represents the time of day.
	attributes: hour, minute, second
	"""
	def print_time(self):
		print '{0:02d}:{1:02d}:{2:02d}'.format(self.hour, self.minute, self.second)
	
	def time_to_int(self):
		seconds = (self.hour * 60**2) + (self.minute * 60**1) + (self.second * 60**0)
		return seconds
	
	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)
	
	def is_after(self, other):
		"""Checks if time1 follows time2.
		self, other: Time objects
		return: Boolean
		"""
		return self.time_to_int() > other.time_to_int()
	
	def __cmp__(self, other):
		t1 = self.time_to_int()
		t2 = other.time_to_int()
		return cmp(t1, t2)
	
def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time
	
	
time1 = Time(10, 12, 36)
time2 = Time(12, 34, 54)

time1 > time2
