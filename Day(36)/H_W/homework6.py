# 6) დაწერე ფუნქცია, რომელიც მიიღებს რიცხვების სიას და გამოიყვანს თითოეულს კვადრატში აყვანილს.

numbers = [3,8,5,7,2,9,4,6]
numbers1 = []
def number(num):  
    for num in numbers:
        numbers1.append(num ** 2)      
    return numbers1
final = number(numbers)    
print(final)  