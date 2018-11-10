import copy
from swampy.World import World

world = World()

my_canvas = world.ca(width = 500, height = 500, background = 'white')
bbox = [[0,0],[100,100]]

# canvas.rectangle(bbox, outline='black', width=2, fill='green4')

class Point(object):
	"""Represents a point in 2-D space.
	atributes: coordinates x, y
	"""

class Circle(object):
	""" Respresents a circle in 2-d space.
	attributes: center point coordinates x, y and radius radius
	"""

	
def draw_point(a, b, canv):
	new_point = [[a,b],[a+2,b+2]]
	draw_rectangle(canv, new_point)
	

def draw_rectangle(canv, rect, color='black'):
	my_canvas.rectangle(rect, fill = color)
	
def make_circle(x, y, r):
	"""Returns coordinates of a circle in 2-D space
	coordinates of center points: x, y
	radius: r
	return: center point and radius
	"""
	new_circle = Circle()
	new_circle.x = x
	new_circle.y = y
	new_circle.r = r
	return new_circle

def draw_circle(circ, outline = None, fill = None):
	my_canvas.circle([circ.x, circ.y], circ.r, outline = outline, fill = fill)

circle_1 = make_circle(10, 50, 100)
circle_2 = make_circle(-100, -40, 60)
circle_3 = make_circle(50, -150, 45)

draw_rectangle(my_canvas, bbox, 'green')
draw_point(25, 150, my_canvas)
draw_point(5, 15, my_canvas)
draw_circle(circle_1, outline = 'black', fill = None)
draw_circle(circle_2, outline = None, fill = 'grey')
draw_circle(circle_3, outline = 'red', fill = None)

# flag of Czech Republic
set_points_1 = [[-150,100], [-150, -100], [0, 0]]
set_points_2 = [[-150,100], [0, 0], [150, 0], [150, 100]]
set_points_3 = [[-150,-100], [0, 0], [150, 0], [150, -100]]

my_canvas.polygon(set_points_1, outline = 'black', fill='blue')
my_canvas.polygon(set_points_2, outline = 'black')
my_canvas.polygon(set_points_3, outline = 'black', fill='red')

world.mainloop()