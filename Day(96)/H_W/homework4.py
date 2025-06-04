# 4)  Is there a vowel in there?

def is_vow(inp):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for i in inp:
        char = chr(i)
        if char in vowels:
            result.append(char)
        else:
            result.append(i)
    return result