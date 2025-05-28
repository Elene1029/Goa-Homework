# 9) Duplicate Encoder

def duplicate_encode(word):
    word_lower = word.lower()  
    result = ''
    
    for char in word_lower:
        if word_lower.count(char) == 1:
            result += '('
        else:
            result += ')'
    
    return result