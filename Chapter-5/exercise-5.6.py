from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()

bob.delay = 0.1

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

def koch(t, n):
    """Draws Koch curve with length n."""
    if n < 3:
        fd(t, n)
        return
    m = n / 3.0
    koch(t, m)
    lt(t, 60)
    koch(t, m)
    rt(t, 120)
    koch(t, m)
    lt(t, 60)
    koch(t, m)

def snowflake(t, n):
    """Draws a snowflake - a triangle with Koch curve for each side"""
    for i in range(3):
        koch(t, n)
        rt(t, 120)

        


