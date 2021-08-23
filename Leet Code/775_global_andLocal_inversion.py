class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if abs(nums[i]-i) > 1:
                return False 
        return True 
        
        