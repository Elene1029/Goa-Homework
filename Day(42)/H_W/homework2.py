# 2) Find the smallest integer in the array

def find_smallest_int(arr):

    n_num = arr[0]
    for i in arr:
        if i < n_num :
            n_num = i
    return n_num   