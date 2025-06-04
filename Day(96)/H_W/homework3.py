# 3 ) Printing Array elements with Comma delimiters

def print_array(arr):
    result = []
    for x in arr:
        result.append(str(x))
    return ",".join(result)