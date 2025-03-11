#3) Check the exam

def check_exam(arr1, arr2):
    num = 0
    for i in range(len(arr1)):
        if arr2[i] == arr1[i]:
            num += 4
        elif arr2[i] == "":
            continue 
        else:
            num -= 1

    return max(num, 0)