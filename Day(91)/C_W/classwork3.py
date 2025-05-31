# 3) შექმენით სია სადაც შეინახავთ სახელებს, და დაასორტირეთ ეს სია ისე რომ ყველაზე მეტი ასო სადაც იქნება ჯერ ეგ რომ იყოს. 


names = ["ნინო", "გიორგი", "ანასტასია", "დათა", "ელენე"]

name_lengths = []
for name in names:
    name_lengths.append((len(name), name))

name_lengths.sort()

result = []
for i in range(len(name_lengths) - 1, -1, -1):
    result.append(name_lengths[i][1])

print(result)