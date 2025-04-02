# 6) Abbreviate a Two Word Name



def abbrev_name(name):
    namme = name.split() 
    return namme[0][0].upper() + '.' + namme[1][0].upper()