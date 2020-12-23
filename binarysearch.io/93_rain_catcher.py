class Solution:
    def solve(self, nums):
        n = len(nums)
        if not n:
            return n
        max_left = [-float('inf')]*n 
        max_right = [-float('inf')]*n 
        max_left[0] = nums[0]
        max_right[-1] = nums[-1]
        
        for i in range(1,n):
            max_left[i] = max(nums[i],max_left[i-1])
        for i in range(n-2,-1,-1):
            max_right[i] = max(nums[i],max_right[i+1])
        
        ans = 0 
        for i in range(n):
            mi = min(max_left[i],max_right[i])
            ans += mi - nums[i]
        
        return ans
                
        