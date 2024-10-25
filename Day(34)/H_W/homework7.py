#7) შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცხვს და დააბრუნებს True, თუ ის ლუწია  და False, თუ არა.

def one():
    while True:
        num = int(input("enter number :"))
        if num % 2 == 0:
            print(True)
        else:
            print(False)   

one()         