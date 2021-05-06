for tt in range(int(input())):
    n,m,k = map(int,input().split())
    k1 = m-1 + m*(n-1)
    if k1 == k:
        print('YES')
    else:
        print('NO')  