fin = open('words.txt')
line = fin.readline()
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print word

        
