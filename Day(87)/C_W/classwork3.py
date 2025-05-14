# 3 ) String cleaning

def string_clean(s):
    string = ''
    for i in s:
        if not i.isdigit():
            string += i
    return string