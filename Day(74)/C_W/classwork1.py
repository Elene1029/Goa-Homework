#1) The @ operator


def evaluate(equation):
    parts = equation.split(" @ ")  
    a = int(parts[0])  
    
    for i in range(1, len(parts)): 
        b = int(parts[i])
        if b == 0:
            return None  
        
        a = (a + b) + (a - b) + (a * b) + (a // b) 
    
    return a

