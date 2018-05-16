def rotate_word(word, n):
    """Rotate a letter in a word by n places within alphabet and creates new, 'rotated' word.

    word: string
    n: integer

    Returns: string ('rotated' word)
    """

    word = word.lower()
    rotated_word = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in word:
        index = alphabet.find(letter)
        index = (index + n) % 26
        rotated_word = rotated_word + alphabet[index]
    return rotated_word



        
    
