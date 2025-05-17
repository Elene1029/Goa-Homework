# 4) შექმენით ფუნქცია, რომელიც დაითვლის სიიდან ყველაზე მეტჯერ რა რიცხვი მეორდება


def number():
    nums = input("Enter numbers separated by commas: ")
    numbers = []
    for x in nums.split(","):
        numbers.append(int(x))

    list_ = []
    max_count = 0
    res = []

    for i in numbers:
        if i not in list_:
            resu = numbers.count(i)
            if resu > max_count:
                max_count = resu
                res = [i]
            elif resu == max_count:
                res.append(i)
            list_.append(i)

    print("Most frequent number(s):", res)