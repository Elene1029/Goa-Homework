# 14)  Simple Simple Simple String Expansion


def string_expansion(s):
    if not s:
        return ""
    
    result = ""
    multiplier = 1  
    
    for ch in s:
        if ch.isdigit():
            multiplier = int(ch)
        else:
            result += ch * multiplier
            
    return result