# 2) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია შემდეგ კი ამ ფუნქციამ უნდა დააბრუნოს უდიდესი რიცხვი ამ სიიდან

numbers =[2,10,99,63,84,39,245,690,56,238,1079]

def my_lists(numbers):
    maxs_num = numbers[0]
    for i in numbers:
        if i > maxs_num:
            maxs_num = i 
    return maxs_num        
print( my_lists(numbers),"ეს იქნება შედეგი ანუ დიდი რიცხვი ")