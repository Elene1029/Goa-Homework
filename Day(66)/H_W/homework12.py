# 12) Moving Zeros To The End


def move_zeros(lst):
    result = []  
    
    for num in lst:
        if num != 0:
            result.append(num) 
    
    result.extend([0] * (len(lst) - len(result))) 
    
    return result