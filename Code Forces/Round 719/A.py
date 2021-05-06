for tt in range(int(input())):
    n = int(input())
    s = input()
    last = dict()
    for i in range(n):
        last[s[i]] = i 
    flag = True
    prev = ""
    last[prev] = -1
    for i in range(n):
        if s[i]!=prev and last[prev]!=i-1:
            flag = False
            break
        prev = s[i]

    if flag:
        print('YES')
    else:
        print('NO')