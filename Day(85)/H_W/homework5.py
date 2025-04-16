# 5) შექმენით ფუნქცია სადაც მომხმარებელს შემოატანინებთ რიცხვს და ამ რიცხვის ჩათვლით შეკრიბავთ ყველა მარტივ რიცხვს.


def sum_primes():
    number = int(input("შეიყვანეთ რიცხვი: "))
    num = 0

    for i in range(2, number + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(f"ნაპოვნია მარტივი რიცხვი: {i}")  
            num += i

    print(f"{number}-მდე არსებული მარტივი რიცხვების ჯამი არის: {num}")
