from sys import stdin 
input = stdin.readline
def multipy(A,B,n):
    result = [[0,0],[0,0]]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k]*B[k][j] 
    
    for i in range(n):
        for j in range(n):
            A[i][j] = result[i][j] 


for t in range(int(input())):
    N = int(input())

    I = [[1,0],[0,1]]
    M = [[0,1],[1,1]] 
    N -= 1
    while (N):
        if N%2:
            multipy(I,M,2)
            N -=1 
        else:
            multipy(M,M,2)
            N /= 2
    print(I[0][0] + I[1][0])