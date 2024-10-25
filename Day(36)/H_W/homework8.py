# 8) დაწერე ფუნქცია, რომელიც იღებს რიცხვს და ამოწმებს, არის თუ არა ის მარტივი რიცხვი.

# number(numb) - ატარებს არგუმენტს numb და შეამოწმებს არის თუ არა მარტივი რიცხვი
# if numb <= 0  თუ რიცხვი ნაკლებია 1-ზე ან ტოლია ფუნქცია დაგვიბრუნებს false-ს ეს იმას ნიშნავს რომ ეს რიცხვი არ იქნება მარტივი
# for i in range(2,numb) - ციკლი რიმელიც ირცევს 2 -დან numb - ის ჩატვლით რიცხვებს
# if numb % i ==0 - თუ numb გაიყოფა i-ზე ნაშთიტ 0 მაშინ numb არ იქნება მარტივი და ისევ დაგვიბრუნებს false-ს
# return true - თუ ყველაფერი მშვიდობით დასრულდა and numb არის მარტივი მაშინ იქნება true 

def number(numb):
    if numb <= 0:
        return False
    for i in range(2, numb):
        if numb % i == 0:
            return False
    return True
numb = int(input("enter num :"))
    
print(number(numb))
