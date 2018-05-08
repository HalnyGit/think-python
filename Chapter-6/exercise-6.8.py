def gcd(a, b):
    if b == 0:
        print a
    else:
        a % b != 0
        gcd(b, (a % b))
    
