class Solution:
    def solve(self, denominations, amount):
        dp = [float("inf")]*(amount+1)
        for i in denominations:
            if i <= amount:
                dp[i] = 1 
        
        for i in range(amount+1):
            for j in denominations:
                if i - j >= 0:
                    dp[i] = min(dp[i-j] + 1, dp[i])
        
        if dp[amount] == float("inf"):
            return -1 
        return dp[amount]


        