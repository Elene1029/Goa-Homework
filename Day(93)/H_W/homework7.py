# 8) Disemvowel Trolls

def disemvowel(string_):
    vowels = "aeiouAEIOU"
    for v in vowels:
        string_ = string_.replace(v, "")
    return string_