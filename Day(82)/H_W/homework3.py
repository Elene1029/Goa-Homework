# 3)Counting sheep...

def count_sheeps(sheep):
    one = 0
    for i in sheep:
        if i == True:
            one  += 1
    return one  