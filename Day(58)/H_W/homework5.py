# 5)  Array.diff

def array_diff(a, b):
    my_list = []
    for i in a:
        if i not in b :
            my_list.append(i)
    return my_list  

# my_list = []  შექმნილია ცარიელი სია რომელშიც შევინახავთ შედეგს
# for i in aლუპი გადის სიის a ყველა ელემენტს
# if i not in b ამოწმებს არის თუ არა ელემენტი i სიის b წევრი
# თუ არ არის ესეიგი b-ში არ გვხვდება ელემენტი უნდა დავამატოთ my_list-ში
# my_list.append(i)  ელემენტი i რომელიც b-ში არ არის ემატება my_list-ს
# return my_list  ბოლოს ფუნქცია აბრუნებს ჩამოყალიბებულ სიას სადაც მხოლოდ ის ელემენტებია რომლებიც b-ში არ გვხვდება       
