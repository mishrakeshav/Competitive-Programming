arr = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
def diagonalDifference(arr):
    l = len(arr)
    rtol = 0
    ltor = 0 
    for i in range(l):
        for j in range(l):
            if(i==j):
                rtol += arr[i][j]
            if(j==l-i-1):
                ltor += arr[i][j]
    print(abs(rtol-ltor))
    

diagonalDifference(arr)