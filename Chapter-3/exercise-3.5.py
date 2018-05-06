def do_twice(f,n):
    f(n)
    f(n)

def print_spam(x):
    print x

def do_four(f,n):
    for i in range(0, 5):
        f(n)


plusMinus = "+ - - - - + - - - - +"
dzielenie = "/         /         /"

def ramka():
    print plusMinus
    for i in range(4):
        print dzielenie
    print plusMinus
    for i in range(4):
        print dzielenie
    print plusMinus


def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print '+ - - - -',

def print_post():
    print '|        ',

def print_beams():
    do_twice(print_beam)
    print '+'

def print_posts():
    do_twice(print_post)
    print '|'

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()
