import math

class Point(object):
	"""Represents a point in 2-D space.
	atributes: coordinates x, y
	"""

blank = Point()
blank.x = 3.0
blank.y = 4.0

point1 = Point()
point1.x = 1.0
point1.y = 1.0

point2 = Point()
point2.x = 4.0
point2.y = 16.0


def distance_between_points(p1, p2):
	dx = (point2.x - point1.x)
	dy = (point2.y - point1.y)
	distance = math.sqrt(dx**2 + dy**2)
	return distance

print distance_between_points(point1, point2)