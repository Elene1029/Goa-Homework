# მოფიქრებული რა 
# append() - ამატებს ელემენტს სიის ბოლოს.

schedule = []
question1 = input("9*9=")
if question1 == "81":
    print(schedule.append(question1))
else:
    print("სიაში არ შევა !")

question2 = input("1+1=")
if question2 =="2":
    print(schedule.append(question2))
else:
    print("სიაში არ შევა!")

question3 = input("6*7=")
if question3 =="42":
    print(schedule.append(question3))
else:
    print("სიაში არ შევა!")

question4 = input("8*7=")
if question4 =="56":
    print(schedule.append(question4))
else:
    print("სიაში არ შევა!")

question5 = input("8*4=")
if question5 =="32":
    print(schedule.append(question5))
else:
    print("სიაში არ შევა!")

question6 = input("6*8=")
if question6 =="48":
    print(schedule.append(question6))
else:
    print("სიაში არ შევა!")

finish = input("გინდა ნახო სია?:")
if finish =="კი":
    print(schedule)
elif finish =="არა":
    print ("ok")    