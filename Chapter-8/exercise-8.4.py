def find(word, letter, start_point = 0):
    index = start_point
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
