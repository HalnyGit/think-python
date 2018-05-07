def is_power(a, b):
    if a / b == 1 or a == 1:
        return True
    if a % b != 0 or b == 1:
        return False    
    return is_power(a / b, b)

        
