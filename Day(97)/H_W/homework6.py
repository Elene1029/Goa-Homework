# 6 ) შექმენით ფუნქცია, რომელიც მომხმარებელს შემოატანინებს რიცხვს და *-ით ისეთი სამკუთხედი დაპრინტეთ რომლის სიმაღლეც იქნება შემოტანილი რიცხვი.

def samkutxedi():
    s = int(input("შეიყვანე მომავალი სამკუთხედის სიმაღლე: "))
    for i in range( s + 1 ):
        print("*" * i)
samkutxedi()