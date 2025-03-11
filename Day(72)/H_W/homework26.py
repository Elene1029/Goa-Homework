# 26) Beginner Series #1 School Paperwork

def paperwork(n, m):
    count = 0
    if n < 0 or m < 0:
        return count
    for i in range (n):
        count += m 
    return count