# 4) How many double digits?

def number_of_duplicate_digits(ndigit):
    numbers = 9*(10 **(ndigit - 1))
    no_numbers = 9 *(9 **(ndigit - 1))
    return numbers - no_numbers

#numbers ყველა n  რიცხვისთვის ეს არის ყველა შესაძლო n-ნიშნა რიცხვი
#no_duplicates n-ნიშნა რიცხვები რომელშიც არ არის თანმიმდევრული ერთი და იგივე ციფრი ეს არის
#რადგან თითოეული ციფრის არჩევისთვის შეგვიძლია აირჩიოთ ნებისმიერი ციფრი გარდა წინანდელის    