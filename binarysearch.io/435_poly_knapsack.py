class Solution:
    def solve(self, w, v ,c):
        dp = [0]*(c+1)
        
        for i in range(c+1):
            for j in range(len(w)):
                if i - w[j] >= 0 :
                    dp[i] = max(dp[i-w[j]] + v[j] , dp[i])
        
        return dp[c]