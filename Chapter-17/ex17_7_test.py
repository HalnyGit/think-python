class Kangaroo(object):
	"""Represents a kangaroo
	attribute: pouch_contents (list)
	"""

	def __init__(self, contents = []):
		self.pouch_contents = []
		self.pouch_contents.extend(contents)
	
	def __str__(self):
		return object.__str__(self)

kanga = Kangaroo()

print kanga
roo = Kangaroo()
print kanga
print roo
print kanga
print roo