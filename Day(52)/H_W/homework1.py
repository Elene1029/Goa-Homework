# 1) Vowel Count

def get_count(sentence):
    asoebi = 0
    aso = "aeiouAEIOU"
    for anbani in sentence:
        if anbani in aso:
            asoebi +=1
    return asoebi  