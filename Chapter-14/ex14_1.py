import os

def walk(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname, name)
		if os.path.isfile(path):
			print path
		else:
			walk(path)

			
def walk2(dirname):
	for root, dirs, files in os.walk(dirname):
		for filename in files:
			print os.path.join(root, filename)


path_1 = 'C:\\' #on Windows, check for whole drive C:
path_2 = 'C:\Users\User\Music' #on Windows, check specific directory
walk2(path_1)


