class Solution:
    def solve(self, matrix):
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        n = len(matrix)
        m = len(matrix[-1])
        def dfs(i,j):
            flag = 1 
            stack = []
            if i == 0 or i == n - 1:
                flag = 0 
            if j == 0 or j == m - 1:
                flag = 0 
            stack.append((i,j))
            
            while stack:
                i,j = stack.pop()
                
                for k in range(4):
                    y = i + dy[k]
                    x = j + dx[k]
                    if 0 <= y < n and 0 <= x < m and matrix[y][x]:
                        if y == 0 or (y == n - 1):
                            flag = 0 
                        if x == 0 or (x == m - 1):
                            flag = 0 
                        stack.append((y,x))
                        
                matrix[i][j] = 0 
            return flag 
        ans = 0 
        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    ans += dfs(i,j)
        
        return ans