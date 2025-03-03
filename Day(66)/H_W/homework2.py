# 2) Counting Duplicates

def duplicate_count(text):
    
    text = text.lower()

    num = {}
    
    for count in text:
        if count in num:
            num [count] += 1
        else:
            num [count] = 1
            
    n = 0 
    
    for v in num.values():
        if v > 1:
            n += 1
    return n  