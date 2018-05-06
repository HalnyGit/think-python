from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()

bob.delay = 0.1


def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n_sides):
    angle = 360.0 / n_sides
    for i in range(n_sides):
        fd(t, length)
        lt(t, angle)

def circle(t, radius):
    circumference = 2 * math.pi * radius
    n_sides = int(circumference / 3) + 1
    length = circumference / n_sides
    polygon(t, length, n_sides)

def arc(t, radius, angle=360.0):
    arc_length = 2 * math.pi * radius * angle / 360
    n_sides = int(arc_length / 3) + 1
    step_length = arc_length / n_sides
    step_angle = float(angle) / n_sides
    for i in range(n_sides):
        fd(t, step_length)
        lt(t, step_angle)
    
    
    

    
