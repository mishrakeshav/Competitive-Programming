for t in range(int(input())):
    n,m = map(int,input().split())
    if n == 1:
        print(0)
    else:
        ans = min(2,n-1)*m 
        print(ans)
            


