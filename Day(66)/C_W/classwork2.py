# 2) Reversed Words

def reverse_words(s):
    words = s.split()
    words.reverse()
    r = ""
    for word in words:
        r += word + " "
    return r.strip()
