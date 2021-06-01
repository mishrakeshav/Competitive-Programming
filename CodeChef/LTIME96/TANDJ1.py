for t in range(int(input())):
    a,b,c,d,k = map(int,input().split())
    steps = abs(a-c) + abs(b-d)
    if steps > k:
        print('NO')
    else:
        k -= steps
        if k %2:
            print('NO')
        else:
            print('YES')