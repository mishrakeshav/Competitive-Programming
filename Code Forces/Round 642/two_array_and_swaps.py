for t in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort(reverse = True)
    s = 0
    i = 0
    j = 0
    
    count = 0
    while i < n and count < k:
        if a[i] < b[j]:
            count += 1
            s += b[j]
            i += 1
            j += 1
        else:
            s += a[i]
            i += 1
    if i < n:
        while i < n:
            s += a[i]
            i += 1
        
    print(s)

    
    
