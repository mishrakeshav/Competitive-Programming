for t in range(int(input())):
    N = int(input())
    A = [0]*9
    for i in range(N):
        a,b = map(int, input().split())
        if a<=8:
            if A[a] < b :
                A[a] = b 
        print(sum(A))
            
            
                

    