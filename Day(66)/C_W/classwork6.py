# 6) Remove exclamation marks

def remove_exclamation_marks(s):
    result = ""
    for char in s:
        if char != '!':
            result += char
    return result