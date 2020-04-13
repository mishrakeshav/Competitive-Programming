for t in range(int(input())):
    N = int(input())
    S = list(map(int,input().split()))
    count = [0]*(N+1)
    for i in S:
        if i <=N:
            count += i 
    print(count)
