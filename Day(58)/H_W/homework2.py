# 2) Small enough? - Beginner

def small_enough(array, limit):
    for i in array:
        if i > limit:
            return False
    return True 

     # for i in array ეს ციკლი გადავა ყველა ელემენტზე
    # if i > limit თუ რომელიმე ელემენტი ლიმიტზე მეტი იქნება
    # ფუნქცია დააბრუნებს false
    # return true თუ ყველა ელემენტი ლიმიტზი ნაკლები ან ტოლი იქნება დააბრუნებს true 