# 2)  Stop gninnipS My sdroW!


def spin_words(sentence):
    words = sentence.split()
    res = []
    for i in words:
        if len(i) >= 5:
            res.append(i[::-1])  
        else:
            res.append(i)
    return ' '.join(res)