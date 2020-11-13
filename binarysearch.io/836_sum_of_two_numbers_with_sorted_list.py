class Solution:
    def solve(self, nums, k):
        
        i = 0 
        j = len(nums) - 1 
        
        while i < j:
            if nums[i] + nums[j] == k:
                return True 
            elif nums[i] + nums[j] > k:
                j -= 1 
            elif nums[i] + nums[j] < k:
                i += 1 
        
        return False 