for t in range(int(input())):
    N = int(input())
    trace = 0 
    j = 0 
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
        trace += matrix[j][j]
        j += 1 
    r = 0 
    c = 0 
    for i in range(N):
        numbers = [0]*(N+1)
        for j in range(N):
            if numbers[matrix[i][j]] :
                r += 1 
                break 
            else:
                numbers[matrix[i][j]] = 1 
    for i in range(N):
        numbers = [0]*(N+1)
        for j in range(N):
            if numbers[matrix[j][i]] :
                c += 1 
                break 
            else:
                numbers[matrix[j][i]] = 1 
    print("Case #{}: {} {} {}".format(t,trace,r,c))
    

