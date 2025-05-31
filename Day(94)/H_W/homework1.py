# 1)  Jaden Casing Strings


def to_jaden_case(string):
    st = string.split()
    new = []
    
    for line in st:
        new.append(line[0].upper() + line[1:].lower())
    return ' '.join(new)