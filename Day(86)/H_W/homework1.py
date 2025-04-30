# 1) შექმენი ფუნქცია,პარამეტრად გადაეცით ორი ცვლადი რომლებიც მიიღებენ მნიშვნელობად ორ სახელებით სავსე სიას,თქვენი დავალებაა გააერთიანო ეს ორი სია ერთ სიაში,გამოიყენეთ სიის ფუნქცია რომელიც დაგეხმარებათ საქმის გამარტივებაში,თუ ვერ გაიხსენებთ მოიძიეთ ინფორმაცია ამ ფუნქციის შესახებ,(ვნახოთ როგორ შეგიძლიათ დამოუკიდებლად რაიმე მცირე ინფორმაციის მოძიება და მისი პრაქტიკაში გამოყენება)

girls_names = ["ele","ana","mari","keso","laura","sandra"]
boys_names  = ["dato","beso","sandro","luka","saba","jeko"]

def my_names(girls_names,boys_names):
    names_list  = []
    names_list.extend(girls_names)
    names_list.extend(boys_names)
    print(names_list)

my_names(girls_names,boys_names)