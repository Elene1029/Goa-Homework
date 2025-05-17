# 7) შექმენით ფუნქცია სადაც მომხმარებელს შემოტანილ რიცხვს გადაიყვანთ ორობით სისტემაში.

def nam():
    number = int(input("შეიყვანეთ მთელი რიცხვი: "))
    if number == 0:
        print("0")
        return
    
    numb = ""
    while number > 0:
        numb = str(number % 2) + numb
        number //= 2

    print("ორობითი სისტემა:", numb)