# 12 ) Find the smallest integer in the array

def find_smallest_int(arr):

    mini_num = arr[0]
    for i in arr:
        if i < mini_num :
            mini_num = i
    return mini_num