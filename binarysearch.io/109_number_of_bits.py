class Solution:
    def solve(self, nums):
        if len(nums)==1:
            if nums[-1] < 0:
                return True 
            return False
        if len(nums) == 0:
            return False 
        total_sum = sum(nums)
        max_sum = -float('inf')
        m = 0 
        for i in nums:
            m = max(m+i,i)
            max_sum = max(m,max_sum)
        
        if max_sum > total_sum:
            return True 
        return False 