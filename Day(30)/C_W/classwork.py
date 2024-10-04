# append = ამატებს ელემენტს სიის ბოლოში.
# append-ის გამოყენება თუ გინდა ბევრჯერ უნდა შექმნა ახლიდან append, რადგან არ შეიძლება 1 append-ით ბევრი ელემენტის დამატება.
# remove = წაშლა
# pop = წაშლა
# extend = ამატებს სიის მითითებულ ელემენტებს
#______________________________________________________________________________________________________________#

#append ვამატებთ სიაში ელემენტს

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

# remove "index-ის გარეშე " სიიდან წავშალეთ ელენე

my_list = ["elene","ana","davit"]

my_list.remove("elene")

print(my_list)

# pop " index-თან ერთად იქნება " სიიდან წავშალეთ ანა

timetable = ["elene","ana","davit"]

timetable.pop(1)

print(timetable)

# სიის სახელის შეცვლა , მის მაგივრად სხვა სახელის დამატება

my_list = ["elene","ana","davit"]

my_list[1] ="me"

print(my_list)

#extend 1 ლისტს დავუმატედ 2 ლისტი

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

list1.extend(list2) 

print(list1)


# აქ ვეუბნებით number-სიიდან გადაიტანოს ლუწი რიცხვები even_numbers სიაში .

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers=[]

for i in range(len(numbers)):
    if numbers[i]%2 ==0:
        even_numbers.append(numbers[i])

print(even_numbers)

