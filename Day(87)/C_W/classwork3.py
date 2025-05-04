# 3) Find the divisors!

def divisors(integer):

    divisors_list = []
    
    for i in range(2, integer):
        if integer % i == 0:
            divisors_list.append(i)
    
    if divisors_list:
        return divisors_list
    else:
        return f"{integer} is prime"