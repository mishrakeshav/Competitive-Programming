for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f = dict()
    for i in a:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    l = len(f)
    m = -1
    for i in f:
        if f[i] > m:
            m = f[i]
    if m <= l - 1:
        print(m)
    else:
        if l <= m - 1:
            print(l)
        else:
            print(l - 1)
