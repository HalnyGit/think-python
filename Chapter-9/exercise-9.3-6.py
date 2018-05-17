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


def avoids(word, letters):
    """Takes a word and a string of letters and returns True
        if the word does not use any of the forbidden letter

        word: string
        letters: string

        return: boolean
    """   
    for letter in letters:
        if letter in word:
            return False
    return True

def check_avoids():
    fin = open('words.txt')
    line = fin.readline()
    counter = 0
    forbidden = raw_input('Enter forbidden letters: ')
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden):
            counter += 1
    print 'Number of words that contain no forbidden letters:', counter


def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True


def check_uses_only():
    fin = open('words.txt')
    line = fin.readline()
    counter = 0
    allowed_only = raw_input('Enter allowed-only letters: ')
    for line in fin:
        word = line.strip()
        if uses_only(word, allowed_only):
            print word
            counter += 1
    print 'Number of words that contain specific letters only:', counter

       
def is_abecedarian(s):
    for i in range(0, len(s)-1):
            if s[i] <= s[i+1]:
                pass
            else:
                return False
    i += 1
    return True
            
    
    
