while True:
        person =(input("რა ოპერაციის არჩევა გსურს +, -, *, // :?:"))
        if person =="+":
            number = int(input("enter your number"))
            number1 = int(input("enter your number"))
            print(number + number1 )
        if person =="-":
            number = int(input("enter your number "))
            number1 = int(input("enter your number"))
            print(number - number1 )
        if person ==" * ":
            number = int(input("enter your nember "))
            number1 = int(input("enter your nember "))
            print(number * number1 )
        if person =="//":
            number = int(input("enter your number"))
            number1 = int(input("enter your number"))
            print(number // number1 )
            
        else:
            print("over")
            break