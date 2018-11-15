class Point(object):
	"""Represents a point in 2-D space.
	atributes: coordinates x, y
	"""
	
	def __init__(self, x = None, y = None):
		self.x = x
		self.y = y
	
	def __str__(self):
		return '{0:d}, {1:d}'.format(self.x, self.y)
	
	def __add__(self, other):
		if isinstance(other, Point):
			return Point(self.x + other.x, self.y + other.y)
		elif isinstance(other, tuple):
			return Point(self.x + other[0], self.y + other[1])
	
	def __radd__(self, other):
		return self.__add__(other)

def print_attributes(obj):
	for attr in obj.__dict__:
		print attr, getattr(obj, attr)
			
		
d = Point(15, 55)
u = Point(10, 25)
p = u + d
k = (40, 80)
a = k + d

print d
print u
print p
print a

print a.__dict__
print_attributes(a)