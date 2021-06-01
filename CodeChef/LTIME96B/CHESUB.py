for t in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    maxx = -float('inf')
    si = 0 
    for i in range(n):
        si = si+a[i]
        maxx = max(maxx,si)
        if si < 0:
            si = 0 
    print(maxx)
