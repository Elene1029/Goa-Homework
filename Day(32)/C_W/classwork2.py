# 2) შექმენით სია სადაც იქნება 10 სახელი შემდეგ ამ სიიდან ამოშლით ყველა იმ სახელს რომელიც იწყება ა ასოზე და დაბეჭდეთ გაფილტრული სია

names = ["aleksandre","leks","anamaria","irakli","anano","ana"]
final =[]

for i in range(len(names)):
    if names [i][0] !="a":
        final.append(names[i])

print(final)        
       
         
    