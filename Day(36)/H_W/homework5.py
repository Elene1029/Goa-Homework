# 5) დაწერე ფუნქცია, რომელიც აბრუნებს ორ რიცხვს შორის მინიმალურ მნიშვნელობას

def number():    
    num = int(input("enter num :"))
    num1 = int(input("enter num :"))
    if num < num1 :
        return num
    else:
        return num1
print (number()) 