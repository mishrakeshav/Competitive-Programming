for t in range(int(input())):
    n,r = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ab = list(zip(a,b))
    ab.sort(key = lambda x : x[0])
    mx = 0 
    k = 0
    j = 0   
    prev = 0 
    for i in range(n):
        k = max(0,k - r*(ab[i][0] - prev))
        k += ab[i][1]
        prev = ab[i][0]
        mx = max(k,mx)

    
    print(mx)

        

