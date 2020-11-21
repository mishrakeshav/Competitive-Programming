class Solution:
    def solve(self, nums):
        inn = False
        dcc = False
        if len(nums) == 1 :
            return True
        elif len(nums) == 0:
            return True
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inn = True
            else:
                inn = False 
                break 
            
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                dcc = True 
            else:
                dcc = False 
                break 
        return inn or dcc
            
