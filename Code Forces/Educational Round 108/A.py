for tt in range(int(input())):
    r,b,d = map(int,input().split())
    r,b = max(r,b),min(r,b)
    diff = r - b 
    if diff == 0:
        print('YES')
        continue
    if diff/b > d:
        print('NO')
        continue
    print('YES')