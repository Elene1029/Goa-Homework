# 1) Basic Mathematical Operations

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    else:
        return "Error"


print(basic_op('+', 10, 5))  
print(basic_op('-', 10, 5)) 
print(basic_op('*', 10, 5)) 
print(basic_op('/', 10, 5))  