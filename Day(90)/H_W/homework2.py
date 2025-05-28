# 2) Descending Order

def descending_order(num):
    digits = list(str(num))
    result = []

    for d in digits:
        inserted = False
        for i in range(len(result)):
            if d > result[i]:
                result.insert(i, d)
                inserted = True
                break
        if not inserted:
            result.append(d)

    return int(''.join(result))
