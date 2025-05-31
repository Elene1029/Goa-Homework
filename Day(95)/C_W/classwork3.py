# 3) Break camelCase

def solution(s):
    res = ""
    for i in s:
        if i == i.upper():
            res += " " + i
        else:
            res += i
    return res