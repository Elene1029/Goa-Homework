#1)Who is going to pay for the wall?

def who_is_paying(name):
    if len(name) <= 2:
        return [name]
    else:
        return [name, name[:2]]