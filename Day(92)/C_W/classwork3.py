# 3)  Return a string's even characters.


def even_chars(st):
    length = len(st)
    if length < 2 or length > 100:
        return "invalid string"
    
    result = []
    i = 1
    while i < length:
        result.append(st[i])
        i += 2
    return result