# 5) დაწერეთ ფუნქცია რომელიც მომხმარებლისგან იღებს რიცხვს და თუ რიცხვი 1-დან 10-მდეა დაბეჭდავს თუარა დაუბეჭდავს "არასწორი რიცხვი"

def one ():
    while True:
        num = int(input("enter number : "))
        if 1 <= num <= 10:
            print("This number is from 1 to 10.")
        else :
            print("This is an invalid number because it is not between 1 and 10.")
one()
