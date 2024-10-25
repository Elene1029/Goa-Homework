# 10) დაწერე ფუნქცია, რომელიც იღებს სიას და აბრუნებს მასში მხოლოდ მარტივ რიცხვებს.


# number(numb) - ატარებს არგუმენტს numb და შეამოწმებს არის თუ არა მარტივი რიცხვი
# if numb <= 1  თუ რიცხვი ნაკლებია 1-ზე ან ტოლია ფუნქცია დაგვიბრუნებს false-ს ეს იმას ნიშნავს რომ ეს რიცხვი არ იქნება მარტივი
# for i in range(2,numb) - ციკლი რიმელიც ირცევს 2 -დან numb - ის ჩატვლით რიცხვებს
# if numb % i ==0 - თუ numb გაიყოფა i-ზე ნაშთიტ 0 მაშინ numb არ იქნება მარტივი და ისევ დაგვიბრუნებს false-ს
# return true - თუ ყველაფერი მშვიდობით დასრულდა and numb არის მარტივი მაშინ იქნება true 
# filt(timetable1) - ირებს სიიდან არგუმენტს timetable-დან და ვქმით ცარიელ სიასა 
# if number(num)- ტუ num მარტივია მაშინ ის დაემატება ახალ სიაში ანუ timetable-ში 
# return timetable - ბოლოს აბრუნებს საბოლოო შედეგს რომოლიც არის მარტო მარტივი ჩვენს timetable-სი რომელიცა განკუთვნილი მარტო მარტივ რიცხვებისთვის 
#  


def number(numb):
    if numb <= 1:  
        return False
    for i in range(2, numb): 
        if numb % i == 0:
            return False
    return True

timetable1 = [2,5,7,9,13,17,13,19,23,28,33,38]
def filt(timetable1):
    timetable = []  
    for num in timetable1:
        if number(num): 
            timetable.append(num)
    return timetable 

print(filt(timetable1)) 

