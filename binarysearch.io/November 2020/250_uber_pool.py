class Solution:
    def solve(self, trips, capacity):
        mx = 0 
        for i in trips:
            mx = max(mx,i[1])
        dp = [0]*(mx+2)
        for i in trips:
            a,b,c = i 
            dp[a] += c 
            dp[b] += -1*c
        for i in range(1,mx+2):
            dp[i] += dp[i-1]
            if dp[i] > capacity:
                return False 
        return True 
        