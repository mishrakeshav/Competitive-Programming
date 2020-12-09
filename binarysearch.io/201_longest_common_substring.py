class Solution:
    def solve(self, s1, s2):
        n = len(s1)
        m = len(s2)
        dp = [ [0 for i in range(n+1)] for i in range(m+1)]
        for i in range(n):
            dp[0][i] = 0 
        for i in range(m):
            dp[i][0] = 0 
        mx = 0 
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    mx = max(mx,dp[i][j])
        return mx