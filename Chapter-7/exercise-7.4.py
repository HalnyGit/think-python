import math

def eval_loop():
    result = 0
    while True:
        s = raw_input('Input data to evaluate or "done" if finished: ')
        if s == 'done':
            break
        else:
            result = eval(s)
            print result
    return result
    
        
    
