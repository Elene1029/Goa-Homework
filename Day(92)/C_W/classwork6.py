# 6) 


def even_fib(n):
    a, b = 0, 1
    total_sum = 0
    
    while a < n:
        if a % 2 == 0:
            total_sum += a
        a, b = b, a + b
    
    return total_sum