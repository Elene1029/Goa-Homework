# 7)Transportation on vacation

def rental_car_cost(d):
    m = 40 
    t = d * m 
    if d >=7:
        t -= 50
    elif d >= 3:
        t -= 20
    return t   
