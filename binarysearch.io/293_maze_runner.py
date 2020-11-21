class Solution:
    def solve(self, matrix):
        di = [0, 1,  0, -1]
        dj = [1, 0 ,-1 ,0]
        n = len(matrix)
        m = len(matrix[-1])
        if matrix[-1][-1] or matrix[0][0]:
            return -1
        def bfs(i,j):
            stack = [(i,j), ]
            matrix[i][j] = 1 
            c = 0 
            while stack:
                new = []
                c += 1 
                for i,j in stack:
                    if (i == n - 1) and (j == m - 1):
                        return c 
                    for k in range(4):
                        x = i + di[k]
                        y = j + dj[k]
                        if 0 <= x < n and 0 <= y < m and (not matrix[x][y]):
                            new.append((x,y))
                            matrix[x][y] = 1
                stack = new 
            return -1 
        return bfs(0,0)