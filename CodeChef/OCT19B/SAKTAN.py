from collections import Counter
for t in range(int(input())):
    a = []
    b = []
    N, M, Q = map(int, input().split())
    for i in range(Q):
        r, c = map(int, input().split())
        r = r - 1
        c = c - 1
        a.append(r)
        b.append(c)
    a = Counter(a)
    b = Counter(b)

    Evenn = 0
    Oddn = 0
    Evenm = 0
    Oddm = 0
    # print(a)
    # print(b)
    for i in range(N):
        if i in a:
            if a[i] % 2 != 0:
                Oddn += 1
            else:
                Evenn += 1
        else:
            Evenn += 1
    for i in range(M):
        if i in b:
            if b[i] % 2 != 0:
                Oddm += 1
            else:
                Evenm += 1
        else:
            Evenm += 1
    print(Oddm * Evenn + Oddn * Evenm)
