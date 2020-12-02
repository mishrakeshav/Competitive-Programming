class Solution:
    def solve(self, n):
        if n<= 3:
            return n 
        dp = [ float('inf') for i in range(n + 1) ]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2 
        dp[3] = 3 
        
        for i in range(4,n+1):
            dp[i] = i 
            for j in range(1,int(math.sqrt(i))+1):
                if j*j > i:
                    break 
                else:
                    dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[n]
            
        
        
                
                
                
        
        