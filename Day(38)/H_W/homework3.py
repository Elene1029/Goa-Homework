# 3) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია შემდეგ კი ფუნქციამ უნდა დააბრუნოს უმცირესი რიცხვი ამ სიიდან


numbers =[2,10,99,63,84,39,-245,690,56,238,-1079]

def my_lists(numbers):
    mini_num = numbers[0]
    for i in numbers:
        if i < mini_num :
            mini_num = i
    return mini_num        
print(my_lists(numbers),"ეს იქნება შედეგი ანუ ყველაზე უმცირესი რიცხვი ამ სიიდან")    