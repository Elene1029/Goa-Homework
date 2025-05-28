# 4) Help Bob count letters and digits.

def count_letters_and_digits(s):
    n = 0
    for x in s:
        if x.isalpha() or x.isdigit():
            n += 1
    return n