# 5) Convert number to reversed array of digits

def digitize(n):
    lists = []
    if n == 0:
        return[0]
    while n > 0:
        lists.append(n % 10)
        n //= 10
    return lists

