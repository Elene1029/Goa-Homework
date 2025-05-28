# 12) Write Number in Expanded Form

def expanded_form(num):
     num_str = str(num)
     length = len(num_str)
     parts = []
 
     for i in range(length):
         digit = num_str[i]
         if digit != '0':
             value = int(digit) * (10 ** (length - i - 1))
             parts.append(str(value))
 
     return ' + '.join(parts)