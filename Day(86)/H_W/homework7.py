# 7)შექმენი ოთხი ცვლადი,შეინახეთ სახელი გვარი ასაკი და სიმაღლე ამ ცვლადებში,შენი დავალებაა გამოიტანო ეს ოთხი მნიშვნელობა ერთ გრძელ წინადადებად შემდეგი ფორმატით -- > ჩემი სახელია name, ჩემი გვარია surname მე ვარ age წლის და ჩემი სიმაღლეა height სანტიმეტრი,გამოიყენეთ string formatting,ეს ავხსენით რამოდენიმე გაკვეთილის წინ და ამაზე ბევრი ვისაუბრეთ,გაიხსენეთ ან გადახედეთ ჩანაწერს

def me(name, surname, age, height):
    result = f"ჩემი სახელია {name}. ჩემი გვარია {surname}. მე ვარ {age}  და ჩემი სიმაღლეა {height}."
    return result


name = "ელე"
surname = "ღარიბოვი"
age = "I'll be as much as you want."
height = 161
over = me(name, surname, age, height)
print(over)