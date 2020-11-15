class Solution:
    def solve(self, matrix):
        n = len(matrix)
        m = len(matrix[-1])
        dp = [[0 for i in range(m)] for i in range(n)]
        dp[-1][-1] = matrix[-1][-1]
        for i in range(n-2,-1,-1):
            dp[i][-1] += dp[i +1 ][-1] + matrix[i][-1]
        for i in range(m-2,-1,-1):
            dp[-1][i] += dp[-1][i+1] + matrix[-1][i]
        
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                dp[i][j] += max(dp[i+1][j], dp[i][j+1]) + matrix[i][j]
        return dp[0][0]