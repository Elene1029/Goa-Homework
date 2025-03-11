# 5) Will there be enough space?


def enough(cap, on, wait):
    return max(on + wait - cap, 0)
