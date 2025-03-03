#5)Are arrow functions odd?


def odds(lst):
    odds = []
    for num in lst:
        if num % 2 != 0:
            odds.append(num)
    return odds
