# 4) მომხმარებელს შეეკითხეთ სახელი შემდეგ შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ მომხმარებლის სახელს შემდეგ კი დააბრუნეთ მომხმარებლის სახელის პირველი ასო მერამდენეა ანბანში


alphabet = "abcdefghijklmnopqrstuvwxyz"

def name(bot): 
    next = bot[0]
    if next in alphabet:
        finish = alphabet.index(next) + 1
        return f"First letter of the name'{next}' is {finish}-ე In alphabetical order."
    else:  
        return "The first letter of the name is not a letter of the alphabet.."

bot = input("enter your name: ")        
print(name(bot))

