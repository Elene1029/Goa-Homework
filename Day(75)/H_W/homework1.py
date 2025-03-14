# 1) Do I get a bonus?


def bonus_time(salary, bonus):
    currency = "$"
    total = 0
    multiplier = 1  

    if bonus:  
        multiplier = 10

    count = 0
    while count < multiplier:
        total += salary
        count += 1

    return currency + str(total)  