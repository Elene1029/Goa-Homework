# 16) მომხმარებელს შემოატანინე თავისი სახელი, შემდეგ კი შეაბრუნე for loop-ის გამოყენებით.

name = input("შეიყვანეთ თქვენი სახელი: ")
reversed_name = ""

for i in name:
    reversed_name = i + reversed_name  

print("შებრუნებული სახელი:", reversed_name)

