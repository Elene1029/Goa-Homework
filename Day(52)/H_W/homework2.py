# 2) Square Every Digit


def square_digits(num):
    result = ""
    for yam in str(num):
        result += str(int(yam) ** 2)
    return int(result)
        