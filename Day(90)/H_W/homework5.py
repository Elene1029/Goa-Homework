# 5 )Extract the domain name from a URL

def domain_name(url):
    start = 0
    if url.startswith("http://"):
        start = 7
    elif url.startswith("https://"):
        start = 8
    if url[start:start+4] == "www.":
        start += 4
    end = start
    while end < len(url) and url[end] != '.':
        end += 1
    return url[start:end]
