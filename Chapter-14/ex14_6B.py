import urllib

zipcode = raw_input('Enter US town zip code: ')
url = 'https://www.uszip.com/zip/' + zipcode
conn = urllib.urlopen(url)
lines = []
for line in conn:
	line = line.strip() + '\n'
	lines.append(line)
conn.close()

name = lines[162][12:]
index_name_end = name.find(',')
name = name[:index_name_end]

population = lines[168]
index_pop_start = population.find('Total population')
population = population[index_pop_start + 25:]
index_pop_end = population.find('<')
population = population[:index_pop_end]

print 'Town: {0:s}, Total population: {1:s}'.format(name, population)