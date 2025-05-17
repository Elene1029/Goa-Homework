# 6) შექმენით ფუნქცია სადაც მომხმარებელს შემოატანინებთ სიტყვას და შეამოწმებთ არის თუ არა ეს სიტყვა პალინდრომე, ოღონდ სიტყვა შეაბრუნეთ for loop-ით. 

def words():
    word = input("შეიყვანეთ სიტყვა: ")
    reversed_word = ""
    
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    
    if word == reversed_word:
        print("ეს სიტყვა არის პალინდრომი.")
    else:
        print("ეს სიტყვა არ არის პალინდრომი.")