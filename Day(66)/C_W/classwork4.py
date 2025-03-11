# 4) Get the mean of an array

def get_average(marks):
    t = 0
    for mark in marks:
        t += mark 
    return t // len(marks)