def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1)

for t in range(int(input())):
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A = sorted(A)
    
    r = A[:K].count(A[K-1])
    n = r + A[K:].count(A[K-1])
    ans = fact(n)//(fact(n-r)*fact(r))
    print(ans)

    







