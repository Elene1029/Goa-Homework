# 7) Will there be enough space?

def enough(cap, on, wait):
    people_left = on + wait - cap

    if people_left < 0:
        return 0
    else:
        return people_left