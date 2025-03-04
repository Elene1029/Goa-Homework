#7) Shortest Word

def find_short(s):
    words = s.split()
    shortest = len(words[0])
    for wor in words:
        if len(wor) < shortest:
            shortest = len(wor)
    return shortest  