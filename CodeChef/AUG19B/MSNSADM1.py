for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    Max = 0
    for i in range(N):
        score = A[i]*20 - B[i]*10
        if score >Max:
            Max = score
        
    print(Max)
    