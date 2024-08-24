# ```1) მომხამრებელს input ის მეშვეობით შემოატანინეთ 2 რიცხვი და შემდეგ ამ ორ რიცხვს შორის ჩაატარეთ უველა არითმეტიკული მოქმედება 
 
num1 = int(input("enter  number: "))
num2 = int(input("enter  numbber: "))

print(num1 - num2)
print(num1 + num2)
print(num1 / num2)
print(num1 % num2)
print(num1 * num2)
print(num1 // num2)
 
#```2) მომხმარებელს input-ის გამოყენებით შემოატანინეთ მისი სახელი და გვარი შემდეგ კი დაუპრინტეთ გრძელი წინადადება 
name = input("enter your name: ")
surname = input("enter your surname: ")

print("gamarjoba, me var " + name + " " + surname)
 

#```3) მომხმარებელს შემოატანინეთ სახელი გვარი, ქალაქი საყავრელი ფერი და საყვარელი საჭმელი. შემდეგ კი ეცადეთ რომ შექმნათ ერთი დიდი გამართული წინადადება

name = input("enter your name: ")
surname = input("enter your surname: ")
city = input("enter your city: ")
color = input("enter your favourite color: ")
food = input("enter your favourite food: ")

print("gamarjoba, chemi saxeli da gvaria " + name + " " + surname + ", adgili sadac me vimyofebi aris " + city + ". chemi sayvareli feria " + color + ", chemi sayvareli sawmelia " + food)

