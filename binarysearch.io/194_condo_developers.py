class Solution:
    def solve(self, matrix):
        n = len(matrix)
        m = len(matrix[-1])
        row = [[-float('inf'),-1] for i in range(n)]
        cols = [[-float('inf'),-1] for i in range(m)] 
        for i in range(n):
            for j in range(m):
                if row[i][0] < matrix[i][j]:
                    row[i][0] = matrix[i][j]
                    row[i][1] = j 
                if cols[j][0] < matrix[i][j]:
                    cols[j][0] = matrix[i][j]
                    cols[j][1] = i 
        INF = float('inf')
        ans = [[INF for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = min(cols[j][0],row[i][0])
        return ans
            