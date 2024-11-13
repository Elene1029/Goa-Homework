# 1) Sum of positive
def positive_sum(arr):
    n = 0
    for u in arr:
        if u >0:
            n += u
    return n