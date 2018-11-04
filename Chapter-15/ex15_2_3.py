import math
import copy

class Point(object):
	"""Represents a point in 2-D space.
	atributes: coordinates x, y
	"""

class Rectangle(object):
	"""Represents a rectangle.
	attributes: width, height, corner
	"""
def print_point(p):
	print '({0:g}, {1:g})'.format(p.x, p.y)

def distance_between_points(p1, p2):
	dx = (point2.x - point1.x)
	dy = (point2.y - point1.y)
	distance = math.sqrt(dx**2 + dy**2)
	return distance

def find_center(rect):
	p = Point()
	p.x = rect.corner.x + rect.width/2.0
	p.y = rect.corner.y + rect.height/2.0
	return p

def grow_rectangle(rect, dwidth, dheight):
	rect.width += dwidth
	rect.height += dheight

def move_rectangle(rect, dx, dy):
	rect.corner.x += dx
	rect.corner.y += dy

def new_rectangle(rect, dx, dy):
	new_rect = copy.deepcopy(rect)
	move_rectangle(new_rect, dx, dy)
	return new_rect

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

center = find_center(box)
# print_point(center)
# print 'width:{0:g}, height:{1:g}'.format(box.width, box.height)
# grow_rectangle(box, 50, 75)
# print 'after growth - width:{0:g}, height:{1:g}'.format(box.width, box.height)
# move_rectangle(box, 50, 75)
# print 'after move - corner.x:{0:g}, corner.y:{1:g}'.format(box.corner.x, box.corner.y)

p1 = Point()
p1.x = 3.0
p1.y = 4.0
print_point(p1)

p2 = copy.copy(p1)
print_point(p2)

box2 = copy.copy(box)

grow_rectangle(box, 50, 50)
print 'box width: {0:g}, box height:{1:g}'.format(box.width, box.height)
print 'box2 width: {0:g}, box height:{1:g}'.format(box2.width, box2.height)

move_rectangle(box, 50, 100)
print 'box corner: {0:g}, {1:g}'.format(box.corner.x, box.corner.y)
print 'box2 corner: {0:g}, {1:g}'.format(box2.corner.x, box2.corner.y)

box3 = copy.deepcopy(box)

grow_rectangle(box, 50, 50)
print 'box width: {0:g}, box height:{1:g}'.format(box.width, box.height)
print 'box3 width: {0:g}, box height:{1:g}'.format(box3.width, box3.height)

move_rectangle(box, 50, 100)
print 'box corner: {0:g}, {1:g}'.format(box.corner.x, box.corner.y)
print 'box3 corner: {0:g}, {1:g}'.format(box3.corner.x, box3.corner.y)

new_box = new_rectangle(box, 17, 23)
print 'box x, y, width, height: {0:g}, {1:g}, {2:g}, {3:g}'.format(box.corner.x, box.corner.y, box.width, box.height)
print 'new_box x, y, width, height: {0:g}, {1:g}, {2:g}, {3:g}'.format(new_box.corner.x, new_box.corner.y, new_box.width, new_box.height)