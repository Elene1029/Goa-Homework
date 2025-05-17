# 3) შექმენით ფუნქცია სადაც მომხმარებელს შემოატანინებთ რიცხვს და გაიგებთ ამ რიცხვიდან თუ ამოდის ფესვი. თუ ფესვი ზუსტად ამოდის მაშინ True დააბრუნოს, სხვა შემთხევაში False

def nam():
    number = int(input("შეიყვანეთ რიცხვი: "))
    if number < 0:
        return False
    
    for i in range(number + 1):
        if i * i == number:
            return True
        if i * i > number:
            break
    
    return False