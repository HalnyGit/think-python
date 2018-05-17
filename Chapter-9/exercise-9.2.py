fin = open('words.txt')
line = fin.readline()

##def has_no_e(word):
##    flag = False
##    for letter in word:
##        flag = flag or letter == 'e'
##    return not flag

def has_no_e(word):
    if not 'e' in word:
        return True
    else:
        return False
    
def no_e_words_only():
    total = 0.0
    count_e = 0.0
    for line in fin:
        word = line.strip()
        total += 1
        if has_no_e(word):
            #print word
            count_e += 1
    print 'Percentage of the words with no "e": {:.2%}'.format(count_e / total)
    


        
