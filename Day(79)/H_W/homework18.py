# 18) მომხმარებელს შემოატანინე ასაკი, თუ ასაკი არის 18-ზე მეტი ან ტოლი, მაშინ დაპრინტეთ რომ არის სრულწლოვანი. თუ შემოიტანა 0-დან 18-მდე მაშინ დაპრინტოს, რომ არასრულწლოვანია. და სხვა შემთხვევაში დაპრინტოს რომ სისტემაში ხარვეზია

age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if age >= 18:
    print("თქვენ ხართ სრულწლოვანი.")
elif 0 <= age < 18:
    print("თქვენ ხართ არასრულწლოვანი.")
else:
    print("სისტემაში ხარვეზია. გთხოვთ სწორად შეიყვანოთ ასაკი.")
