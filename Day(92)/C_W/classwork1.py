# 1)  Reversing Words in a String

def reverse(st):
    words = st.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)