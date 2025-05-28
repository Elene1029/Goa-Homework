# 3) Detect Pangram

def is_pangram(st):
    st = st.lower()
    found = set()

    for ch in st:
        if 'a' <= ch <= 'z':
            found.add(ch)

    return len(found) == 26