class Solution:
    def solve(self, nums):
        dp = dict()
        def helper(pos):
            if pos >= len(nums):
                return  -float('inf')
            if pos in dp:
                return dp[pos]
            else:
                dp1 = helper(pos + 1)
                dp2 = helper(pos + 2)
                ans = nums[pos] + max(dp2,0) 
                ans = max(dp1,ans)
                ans = max(ans,0)
                dp[pos] = ans 
                return ans 
        
        return helper(0)
                
                
            
        