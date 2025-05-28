# 10 ) Replace With Alphabet Position

def alphabet_position(text):
    result = []
    for char in text.lower():
        if char.isalpha():
            pos = ord(char) - ord('a') + 1
            result.append(str(pos))
    return ' '.join(result)