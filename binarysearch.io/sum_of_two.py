class Solution:
    def solve(self, nums, k):
        # Write your code here
        ki = {}
        
        for i in nums:
            if i not in ki:
                ki[i] = 1
            else:
                ki[i] =1
        if len(nums) == 1:
            return False
        for i in nums:
            if k-i in ki:
                return True
        return False
            
        
