# 2) შექმენით ფუნქცია სადაც მომხმარებელს შემოატანინებთ რიცხვს. და ეს რიცხვი გაყავით ამ რიცხვის ციფრთა ჯამზე. (დავუშვათ შემოიტანა მომხმარებელმა 150. ანუ 150 უნდა გაყოს 6-ზე, რადგან 1+5+0 = 6)

def nam():
    number = int(input("შეიყვანეთ რიცხვი: "))
    num_str = str(abs(number)) 

    digit_sum = 0
    for d in num_str:
        digit_sum += int(d)
    
    if digit_sum == 0:
        print("ვერ გაამრავლებ 0-ზე.")
    else:
        result = number / digit_sum
        print(f"{number} / {digit_sum} = {result}")