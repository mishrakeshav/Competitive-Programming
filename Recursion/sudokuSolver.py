import numpy as np

n = 9
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))


def isValid(y,x,n):
    global grid
    for i in range(9):
        if grid[y][i] == n:
            return False
    for j in range(9):
        if grid[j][x] == n:
            return False
    
    xrange = (x//3)*3
    yrange = (y//3)*3 
    for i in range(0,3):
        for j in range(0,3):
            if grid[yrange + i][xrange + j] == n:
                return False
    return True

def solve():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for k in range(1,10):
                    if isValid(i,j,k):
                        grid[i][j] = k
                        solve()
                        grid[i][j] = 0 
                return
    print(np.matrix(grid))

solve()