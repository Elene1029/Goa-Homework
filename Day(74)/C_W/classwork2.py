#2)Pythagorean Triple

def pythagorean_triple(integers):
    a, b, c = integers  
     
    if a > b and a > c:
        a, c = c, a  
    elif b > a and b > c:
        b, c = c, b  
    
    return a**2 + b**2 == c**2