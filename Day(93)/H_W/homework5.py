# 5) Age Range Compatibility Equation

def dating_range(age):
    if age <= 14:
        min = age - 0.10 * age
        max = age + 0.10 * age
    else:
        min = (age/2)+7
        max = (age-7)*2
        
    return str(int(min))+'-'+str(int(max))