class Solution:
    def solve(self, matrix):
        n = len(matrix)
        m = len(matrix[-1])
        dp = [[0]*m for i in range(n)]
        mx = 0 
        for i in range(n):
            for j in range(m):
                dp[i][j] = matrix[i][j]
                if matrix[i][j] and i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1 
                mx = max(mx,dp[i][j])
        return mx**2