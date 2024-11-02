# 1) შექმენით კალკულატორის ფუნქცია რომელსაც ექნება სამი პარამეტრი პირველი რიცხვი, მეორე რიცხვი და მოქმედება თუ რა მოქმედება უნდა რომ შესრულდეს ამ ორ რიცხვს შორის რიცხვებიდან და მათემატიკური ოპერატორიდან გამომდინარე დაგიბრუნოთ პასუხი, თუ მაგალითად მომხმარებელამ შემოიტანა 5 და 10 ხოლო მას უნდა ამ ორი რიცხვის დამატება ანუ მესამე პარამეტრი არის "+" პლიუსი ეს ორი რიცხვი შეიკრიბოს 5 + 10 = 15


def canculator():
    operators = input("which operator do you want to choose?'+','-','*','/'")
    num1 = int(input("enter num :"))
    num2 = int(input("enter num :"))
    if operators == "+":
        return num1 + num2
    elif operators =="-" :
        return num1 - num2
    elif operators == '*':
        return  num1 * num2
    elif operators == '/':
        return num1 /num2   
    else:    
        return "error "

print("result:",canculator())  
            