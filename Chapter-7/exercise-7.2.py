def square_root(a, x, epsilon):
    while True:
        print x
        y = (x  + a/x) / 2
        if abs(y - x) < epsilon:
            break
        x = y

        
