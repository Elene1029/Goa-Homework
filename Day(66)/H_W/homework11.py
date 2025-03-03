# 11) Moving Zeros To The End


def move_zeros(lst):
    position = 0 
    
    for num in lst:
        if num != 0:
            lst[position] = num
            position += 1
            
    for i in range(position, len(lst)):
        lst[i] = 0
        
    return lst