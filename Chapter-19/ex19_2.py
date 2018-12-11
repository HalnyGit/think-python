from swampy.Gui import *

g = Gui()
g.title = ('Gui')

	
def make_circle():
	item = canvas.circle([0,0], 100, fill='red')

canvas = g.ca(width=500, height=500)
canvas.config(bg='white')
	
g.bu(text='Circle maker', command = make_circle)

g.mainloop()