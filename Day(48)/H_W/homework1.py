# Cat years, Dog years

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    elif human_years  >2:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2 ) * 5
    else:
        return " error"
        
    return[human_years, cat_years,dog_years]    