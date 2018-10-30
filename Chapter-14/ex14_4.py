import os

def find_mp3(dirname):
	res = []
	for root, dirs, files in os.walk(dirname):
		for filename in files:
			if filename.endswith('.mp3'):
				res.append(os.path.join(root, filename))
	return res

def get_file_sum(filename):
	cmd = 'CertUtil -hashfile ' + filename + ' MD5'
	fp = os.popen(cmd)
	res = fp.readlines()
	fp.close()
	return res[1]

def get_duplicates(file_list):
	sum_file_map = dict()
	duplicates = []
	for filename in file_list:
		sum = get_file_sum(filename)
		sum_file_map.setdefault(sum, []).append(filename)
	for sum in sum_file_map:
		if len(sum_file_map[sum]) > 1:
			duplicates.append((sum_file_map[sum]))
	return duplicates
	
		
file_list = find_mp3('C:\Users\Komp\Music')
duplicates = get_duplicates(file_list)
for i in duplicates:
	print i



