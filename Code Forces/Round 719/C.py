for tt in range(int(input())):
    n = int(input())
    if n==2:
        print(-1)
        continue
    a = 1 
    matrix = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i%2==1 and  j%2==0:
                matrix[i][j] = a 
                a += 1 
            elif i%2==0 and j%2==1:
                matrix[i][j] = a
                a += 1 
        
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==0:
                matrix[i][j] = a 
                a += 1 

    for m in matrix:
        print(*m)
