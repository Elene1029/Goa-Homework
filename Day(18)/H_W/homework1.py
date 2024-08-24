#  1) შექმენით ბანკის სისტემა სადაც იქნება ძალიან ბევრი პირობები და გამოიყენებთ if, elif და else -ს, გამოიყენებთ ასევე განვლილ მასალასაც  .     


def show_balance():     # def - ქმინს ფუნქციას და ინახავს მასში მოთავსებულ კოდს.   # აქ გვიჩვენებს ბალანს                                        
    print(f"ეს არის შენი ბალანსი >  ${balance:2f}.")    # f რიცხვს ამრგვალებს ორ ათწილამდე. 


def cash_in():  # ფუნქცია რის მეშვეობით ბალანსში ვდებთ თანხას.
    cash = int(input(" რამდენი თანხის შეტანა გსურს"))
    if cash < 0:
        print ("უარყოფით თანხას ვერ შეიტან")
        return 0 # return   ფუნქციიდან გასვლას და მნიშვნელობის დაბრუნებას ნიშნავს.
    else: 
        return cash


 
def withdrow():   # ფუნქცია რის მეშვეობით ბალანსიდან ვიღებთ თნხას.
    cash = int(input("რამდენი თანხის გამოტანა გსურს?"))
    if cash > balance:
        print("შენ არ გაქვს ბალანსზე ამდენი თანხა!")
        return 0      # return   ფუნქციიდან გასვლას და მნიშვნელობის დაბრუნებას ნიშნავს.
    elif cash < 0:
        print("თანხას რომელსაც სჰენ გამოიტან უნდა იყოს 0 ზე მეტი!!!!")
        return 0      # return   ფუნქციიდან გასვლას და მნიშვნელობის დაბრუნებას ნიშნავს.   
    else:
        return cash   # return   ფუნქციიდან გასვლას და მნიშვნელობის დაბრუნებას ნიშნავს.

balance = 0 
bank_online = True
while bank_online:  # while loop-ით ჩვენ შეგვიძლია შევასრულოთ განცხადებები, სანამ პირობა არის true.
    print("                                                                                                                                               WELLCOME  TO  THE  BANK                  ")
    print("""
1 show balance
2 witdrow
3 cash in 
4 exit

""")
    operation = (input("რომელი ოპერაციის არჩევა გსურს?   "))
    if operation == '1':
        show_balance()



    elif operation == "2":
       balance= balance - withdrow()



    elif operation == "3":
        balance = balance + cash_in()


    elif operation == "4":
        print("                                                                                                                                                                                                                                                                       <    მობრძანდით კიდე ერთხელ   >  ")
        bank_online = False 


    else:
        print("")