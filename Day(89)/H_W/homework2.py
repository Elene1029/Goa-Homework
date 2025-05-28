# 2 ) Is every value in the array an array

def arr_check(arr):
    for x in arr:
        if isinstance(x, list):
            continue
        else:
            return False
    return True