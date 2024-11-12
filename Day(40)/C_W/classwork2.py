# 2) Hello, Name or World!
#capitalize - ადიდედბ პირველ ასოს.

def hello(name=None):
    if not name:
        return("Hello, World!")
    return("Hello, " + name.capitalize() + "!")
    