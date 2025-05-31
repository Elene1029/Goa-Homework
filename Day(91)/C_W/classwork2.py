# 2) Alien Accent

def convert(st):
    result = ""
    for i in st:
        if i == "a":
            result += "o"
        elif i == "o":
            result += "u"
        else:
            result += i
    return result
