# 2) They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?

def is_opposite(s1, s2):
    if s1 == "" or s2  == "":
        return False
    for chr in range(0,len(s1)) :
        if  s1[chr] == s2[chr]:
            return False
    else:
        return True