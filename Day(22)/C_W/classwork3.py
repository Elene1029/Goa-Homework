# 3) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ while loop ის გამოყენებით 1-დან მომხმარების შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ ხუთის ჯერადი რიცხვები

num = int(input("enter num: "))
number = 0 


while number < num:
    if number %5 == 0:
        print(str(number)+ "5  ის ჯერადია")
    else:
        print(str(number)+ "არარის")
number = number + 1           