def power(base,p):
    result = 1 
    while p:
        if p%2 :
            result *= base 
            p -= 1 
        else:
            p /= 2 
            base *= base 
    return result 
print(power(20,2))