"""
4 2 3 4 2 3 4 2 3
1 2 3 4 5 6 7 8 9

5 2 3 4 5 2 3 4 5 2 3 4

"""
for t in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    freq = [dict() for i in range(k)]
    for i in range(n):
        if arr[i] not in freq[i%k]:
            freq[i%k][arr[i]] = 1 
        else:
            freq[i%k][arr[i]] += 1 
    
    ans = 0 
    for i in range(k):
        total = 0 
        maxx = -1 
        for a,b in freq[i].items():
            total += b 
            maxx = max(maxx,b)
        ans += total - maxx 
    
    print(ans)

