#  2) შექმენით ფუნქცია რომელიც მომხმარებელს ეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი

def number():
    num = int(input("enter num"))
    
    if num % 2 == 0:
        print("this is even")
    else:
        print("this is odd")

number()        
