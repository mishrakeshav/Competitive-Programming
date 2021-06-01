for t in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    if k == 1:
        maxx = -float('inf')
        si = 0 
        for i in range(n):
            si = si+a[i]
            maxx = max(maxx,si)
            if si < 0:
                si = 0 
        print(maxx)
    elif k == 2:
        maxx = -float('inf')
        si = 0 
        prefix = []
        for i in range(n):
            si = si+a[i]
            maxx = max(maxx,si)
            if si < 0:
                si = 0 
            prefix.append(maxx)
        suffix = [0 for i in range(n)]
        si = 0 
        maxx = -float('inf')
        for i in range(n-1,-1,-1):
            si = si+a[i]
            maxx = max(maxx,si)
            if si < 0:
                si = 0 
            suffix[i] = maxx
        ans = -float('inf')
        for i in range(n-1):
            ans = max(ans,prefix[i] + 2*suffix[i+1])
        print(ans)