# 2)შექმენით ფუნქცია სახელად addition,პარამეტრად გადაეცით ცვლადი და არგუმენტად გადაეცით სია სადაც მოთავსებული გექნებტ რიცხვები,თქვენი დავალებაა იპოვოთ ამ სიაში მოთავსებული რიცხვების ჯამი


def addition(numbers):
    number = 0
    for i in numbers:
        number += i
    return number

my_list = [3, 7, 92, 5]
r = addition(my_list)
print("რიცხვების ჯამი არის:", r)
