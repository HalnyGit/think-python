class Kangaroo(object):
	"""Represents a kangaroo
	attribute: pouch_contents (list)
	"""

	def __init__(self, contents = None):
		self.pouch_contents = []
		if contents == None:
			contents = []
		self.pouch_contents.extend(contents)
	
	def __str__(self):
		t = [object.__str__(self) + ' with pouch contents:']
		for obj in self.pouch_contents:
			s = '   ' + object.__str__(obj)
			t.append(s)
		return '\n'.join(t)
			
	def put_in_pouch(self, other):
		self.pouch_contents.append(other)

kanga = Kangaroo(['apple', 'banana'])
roo = Kangaroo()
print kanga
print roo
kanga.put_in_pouch(roo)
print kanga
kanga.put_in_pouch('plum')
print kanga
print roo