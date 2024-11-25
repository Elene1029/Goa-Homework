# 6) Counting sheep

def count_sheeps(sheep):
    tally = 0
    for i in sheep:
        if i == True:
            tally += 1
    return tally     