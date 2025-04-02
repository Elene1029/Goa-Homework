# 1) Find numbers which are divisible by given number


def divisible_by(numbers, divisor):
    my_list = []
    for i in numbers:
        if i % divisor == 0:
            my_list.append(i)
    return my_list

