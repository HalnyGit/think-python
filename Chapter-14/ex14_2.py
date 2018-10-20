import os
import string


def sed(patern, replacement, infile, outfile):
	"""Reads infile and writes its content to outfile
	and replacing patern string with replacement string
	patern: string
	replacement: string
	infile: file
	outfile: file
	"""
	try: 
		fin = open(infile, 'r')
		fout = open(outfile, 'w')
	
		for line in fin:
			line = line.replace(patern, replacement)
			fout.write(line)
	
		fin.close()
		fout.close()
	except:
		print 'Error'

sed('Emma', 'Ana', 'test.txt', 'output.txt')
	
	
