# 2) Find The Parity Outlier


def find_outlier(integers):
    odd_count = 0
    even_count = 0

    for num in integers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if odd_count > 1 and even_count > 0:
            break
        if even_count > 1 and odd_count > 0:
            break

    for num in integers:
        if odd_count == 1 and num % 2 != 0:
            return num
        if even_count == 1 and num % 2 == 0:
            return num
            
 # ესეიგი პირველი მოქმედება ციკლი ითვლის 
 # ლუწის და კენტის რიცხვების ჯამს უი რაოდენობას 
 #  როცა 1 ტიპის რიცხვი 2 ეს შორის მედია მოქმედება მანდ წყდება
 # მეორე ციკლში ვეძებთ იმას რიცხვს რომელიც უმრავლესობაშია
 # შემდეგ ან კენტს თუ უმრავლესობა ლუეია ან პირიქით ანუ ლუწს უმრავლესობა კენტი იქნება რა 
 # და დავაბრუნებთ ვაბრუნებთ მას ვსო 