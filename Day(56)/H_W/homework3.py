# 3) Take a Ten Minutes Walk


def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    return walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
    
    # ანუ ჯერ ამოწმებს სია ვალკ 10 ელემენრი უნდა იყოს ანუ 
    # 10 ნაბიჯი რო 10 წუთია რა და 10 ნაბიჯი თუარა falseს დააბრუნება
    # მერე count n ჩრდილოეთში მიმართულაბას ითვლის სამხრეთისაც მერე ეგენი
    # ტოლი უნდა იყოს რომ საწყისში დამთავრდეს გასეირნება და ისევ იგივე ემართება
    # აღმოსავლეთსაც დასავლეთსაც