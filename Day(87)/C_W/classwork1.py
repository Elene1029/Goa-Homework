 # 1) How good are you really?

def better_than_average(class_points, your_points):
    total = 0 
    for i in class_points:
        total += i 
    over = total / len(class_points)
    return your_points > over 