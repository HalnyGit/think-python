from swampy.Gui import *

g = Gui()
g.title = ('Gui')

def make_button():
	g.bu(text = 'Label maker', command = make_label) 
	
def make_label():
	g.la(text='Nice job!')

g.bu(text='Button maker', command = make_button)

canvas = g.ca(width=500, height=500)
canvas.config(bg='white')

item = canvas.circle([0,0], 100, fill='red')
item.config(fill='yellow', outline='orange', width=10)


g.mainloop()