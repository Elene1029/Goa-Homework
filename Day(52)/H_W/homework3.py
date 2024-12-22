# 3) Highest and Lowest


def high_and_low(numbers):
    num = numbers.split()
    g = int(num[0])
    w = int(num[0])
    
    for nums in num:
        nums = int(nums)
        if nums > g:
            g = nums
        elif nums < w:
            w = nums
        
    return F"{g} {w}"