# 4) შექმენით ფუნქცია სადაც მომხმარებელი შეიყვანს ორ რიცხვს და ოპერაციას. რა ოპერაციასაც აირჩევს მომხმარებელი ის მოქმედება უნდა შეასრულოთ და ეს დააბრუნეთ f სტრინგის გამოყენებით.

def calculate():
    num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
    operation = input("აირჩიეთ ოპერაცია (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "შეცდომა: ვერ დაყოფა 0-ით"
    else:
        return "შეცდომა: არასწორი ოპერაცია"

    return f"ოპერაცია: {num1} {num2} {operation} = {result}"


print(calculate())