# 4) დაწერე ფუნქცია, რომელიც input()-ით იღებს ორ რიცხვს და ბეჭდავს, რომელია დიდი.

def one ():
    while True:
        num1 = int(input("enter number : ")) 
        num2 = int(input("enter number :"))

        if num1 > num2:
            print(num1)
        elif num2 > num1:
            print(num2)     

one()        