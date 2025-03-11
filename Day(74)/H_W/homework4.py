# 4) Calculate average


def find_average(numbers):
    
    if not numbers:
        return 0
    t = 0
    for num in numbers:
        t += num  
    return t / len(numbers)
