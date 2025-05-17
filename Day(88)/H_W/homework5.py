# 5) შექმენით ფუნქცია სადაც მომხმარებელს შემოატანინებთ სიტყვას და ამ სიტყვას დააბრუნებთ ისე რომ ხმოვნები იყოს დაფარული

def vowels():
    vowels = "aeiouAEIOU"
    word = input("შეიყვანეთ სიტყვა: ")
    res = ""
    for i in word:
        if i in vowels:
            res += "*"
        else:
            res += i
    return res