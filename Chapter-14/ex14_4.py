import os

def find_mp3(dirname):
	res = []
	for root, dirs, files in os.walk(dirname):
		for filename in files:
			if filename.endswith('.mp3'):
				res.append(os.path.join(root, filename))
	return res

def check_file_sum(file_list):
	for filename in file_list:
		cmd = 'CertUtil -hashfile ' + filename + ' MD5'
		fp = os.popen(cmd)
		res = fp.read()
		print res
		fp.close()

file_list = find_mp3('C:\Users\Komp\Music')
check_file_sum(file_list)




