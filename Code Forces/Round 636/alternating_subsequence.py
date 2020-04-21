from sys import stdin
input = stdin.readline
for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = 0
    i = 0
    m = a[0]
    while i != n-1 and a[i] < 0:
        m = max(a[i],m)
        i += 1
    if i == n-1:
        s = m
    alt = 1
    while i!=n-1:
        
        if alt == 1:
            while i != n-1 and a[i] < 0:
                i += 1
            prev = a[i]
            while i != n-1 and a[i] > 0 :
                prev = max(a[i], prev)
                i += 1
            s += prev
            alt = 0
        else:
            while i != n-1 and a[i] > 0:
                i += 1
            prev = a[i]
            while i != n-1 and a[i] < 0:
                if a[i] < 0:
                    prev = max(a[i], prev)
                i += 1
            s += prev
            alt = 1
    print(s)

