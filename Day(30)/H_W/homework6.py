# 6) შექმენით სია სადაც იქნება 20 განსხვავებული რიცხვი, შექმენით ორი ახალი სია ერთი ლუწებისთვის მეორე კენტებისთვის ორივე იქნება თავდაპირველად ცარიელი, გაფილტრეთ სია რომელშიც არის 20 განსხვავებული რიცხვი ამ სიიდან ამოარჩიეთ ყველა ლუწი რიცხვი და დაამატეთ ლუწებისთვის განკუთვნილ სიაში ხოლო კენტები კენტებისთვის განკუთვნილ სიაში

numbers = [18,49,38,23,29,11,79,39,34,74,53,94,99,63,77,90,51,41,27,69]

even_numbers = []

odd_numbers = []

for i in range(len(numbers)):
    if numbers[i]%2 ==0:
        even_numbers.append(numbers[i])
    else:
        odd_numbers.append(numbers[i])   

print(odd_numbers,"odd")
print(even_numbers,"even")








