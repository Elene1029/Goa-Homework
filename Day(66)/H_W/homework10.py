# 10) Sum of Triangular Numbers


def sum_triangular_numbers(n):
    if n < 0:
        return 0

    num = 0
    for i in range(1, n + 1):
        number = i*(i + 1) // 2
        num += number
        
    return num   