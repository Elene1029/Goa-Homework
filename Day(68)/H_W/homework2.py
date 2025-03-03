#2)Find Multiples of a Number
 

def find_multiples(integer, limit):
    lists = []
    for i in range(integer, limit + 1, integer):
        lists.append(i)
    return lists