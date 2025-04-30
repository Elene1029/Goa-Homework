# 3)შექმენით ფუნქცია,პარამეტრად გადაეცით ცვლადი,რომელიც მიიღებს მნიშვნელობად სტრინგს --> "ale4qs6and3re'' , შენი დავალებაა ამ სტრინგიდან ამოშალო ყველა რიცცხვი და დააბრუნო ეს სტრინგი რიცხვების გარეშე

def num(text):
    r = ""
    digits = "0123456789"
    for i in text:
        if i not in digits:
            r += i
    return r

name = "ale4qs6and3re"
over = num(name)
print(over)