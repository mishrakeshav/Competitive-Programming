class Solution:
    def solve(self, n, k):
        
        def helper(i,k):
            if (i,k) in dp:
                return dp[(i,k)]
            if i > n:
                return 0 
            if i == n:
                return 1 
            ans = helper(i+2,k)
            ans += helper(i+1,k)
            if k:
                ans += helper(i+3,k-1)
            dp[(i,k)] = ans 
            return ans
        
        dp = dict()
        return helper(0,k)