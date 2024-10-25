# 1) დაწერე ფუნქცია, რომელიც იღებს ორი რიცხვის მნიშვნელობას input() საშუალებით და ბეჭდავს მათ ჯამს

def one():
    while True:
        question = input("Which function would you like to use?: +,-,*,// : ")
        person1 = int(input("enter number :"))
        person2 = int(input("enter number :"))
        if question  == "+":
            print( person1 + person2)
        elif question == "-" :
            print(person1 - person2 )     
        elif question == "*":
            print(person1 * person2)    
        elif question == "//" :
            print(person1 // person2)    

one()