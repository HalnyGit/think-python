# checks only first letter
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
        
# refers only to 'c' letter
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return True
        else:
            return False

# returns only last letter check
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# OK
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# checks only until first upper letter
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
