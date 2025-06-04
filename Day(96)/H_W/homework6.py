# 6) Delete occurrences of an element if it occurs more than n times


def delete_nth(order,max_e):
    answer = []
    for x in order:
        if answer.count(x) < max_e:
            answer.append(x)
            
    return answer