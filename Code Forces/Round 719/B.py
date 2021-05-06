for tt in range(int(input())):
    n = int(input())
    ans = 0
    k = 1 
    while k <= n:
        for d in range(1,10):
            if d*k <= n:
                ans += 1
        k = k*10 + 1     
    print(ans)



