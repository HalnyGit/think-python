from math import sqrt

def square_root(a, epsilon):
    x = float(a) / 2
    while True:
        y = (x  + a/x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return y


def square_root_comp(epsilon):
    for a in range(1, 10):
        result1 = square_root(a, epsilon)
        result2 = sqrt(a)
        delta = abs(square_root(a, epsilon) - sqrt(a))
        print '{0:1d} {1:13.11f} {2:13.11f} {3:13.11e}'.format(a, result1, result2, delta)



        
        
    
