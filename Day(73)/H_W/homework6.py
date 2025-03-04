#6) Did she say hallo?


def validate_hello(greetings):
    greetings = greetings.lower()  
    for word in ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]:
        if word in greetings:  
            return True
    return False 