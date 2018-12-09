class Hist(dict):
	"""A map from each item (x) to its frequency."""

	def __init__(self, seq=[]):
		"Creates a new histogram starting with the items in seq."
		for x in seq:
			self.count(x)

	def count(self, x, f=1):
		"Increments the counter associated with item x."
		self[x] = self.get(x, 0) + f
		if self[x] == 0:
			del self[x]
			

s = 'ssssstringgg'

lhist = Hist()
for char in s:
	lhist.count(char)

for key, value in lhist.iteritems():
	print key, value
