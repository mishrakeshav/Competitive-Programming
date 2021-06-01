import string 
for t in range(int(input())):
    k,*s = list(input().split())
    k = int(k)

    first = string.ascii_lowercase[:13]
    second = string.ascii_uppercase[13:]
    for char in s:
        if char.lower() == char:
            flag = all([(i in first) for i in char])
        elif char.upper() == char:
            flag = all([(i in second) for i in char]) 
        else:
            flag = False
            break
        if flag == False:
            break
    if flag:
        print('YES')
    else:
        print('NO')
        