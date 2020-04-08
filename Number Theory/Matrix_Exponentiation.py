from sys import stdin 
input = stdin.readline
def multipy(A,B,n):
    result = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k]*B[k][j] 
    
    for i in range(n):
        for j in range(n):
            A[i][j] = result[i][j] 

for i in range(int(input())):
    n,p = map(int,input().split())
    A = []
    I = [[0 for i in range(n)] for j in range(n)]
    j = 0
    for i in range(n):
            A.append(list(map(int, input().split())))
            I[i][j] = 1 
            j += 1 
    while p:
        if p%2:
            multipy(I,A,n)
            p -= 1 
        else:
            multipy(A,A,n)
            p /= 2

    for i in range(n):
        for j in range(n):
            print(I[i][j], end = " ")
        print() 
    
        
        

