# 6) Invert values

def invert(lst):
    result = []
    for x in lst:
        if x == 0:
            result.append(0) 
        else:
            result.append(0 - x) 
    return result