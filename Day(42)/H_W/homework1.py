# 1) Reversed Strings

def solution(string):
    r = ''
    for d in string:
        r = d + r
    return r    