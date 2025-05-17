# 1 )   Sum without highest and lowest number

def sum_array(arr):
    if not arr or len(arr) <= 1 :
        return 0
    return sum(arr) - max(arr) - min(arr)