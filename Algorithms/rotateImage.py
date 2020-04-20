N = int(input())
matrix = [] 
for i in range(N):
        matrix.append(list(map(int, input().split())))
     
for i in range(N):
    for j in range(N): 
        if i < j :
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            
for i in range(N):
    for j in range(N//2):
        matrix[i][j],matrix[i][N-1-j] = matrix[i][N-1-j],matrix[i][j]
    
for i in range(N):
    print(matrix[i])

    