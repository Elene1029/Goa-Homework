#4)Sum of two lowest positive integers


def sum_two_smallest_numbers(numbers):
    num = min(numbers)
    numbers.remove(num)
    nums = min(numbers)
    return num + nums