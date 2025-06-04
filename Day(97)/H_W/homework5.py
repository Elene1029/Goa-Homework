# 5 )  Convert string to camel case



def to_camel_case(text):
    text = text.replace("_", "-")  
    split = text.split("-")        

    if not split:
        return ""

    result = [split[0]] 

    for elem in split[1:]:
        result.append(elem.capitalize())  

    return ''.join(result)