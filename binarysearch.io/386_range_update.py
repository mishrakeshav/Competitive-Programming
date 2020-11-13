class Solution:
    def solve(self, nums, operations):
        converted = [0]*(len(nums))
        for x,y,z in operations:
            converted[x] += z 
            if (y+1) < len(converted):
                converted[y+1] -= z 
        
        for i in range(1,len(converted)):
            converted[i] += converted[i-1]
        
        for i in range(len(nums)):
            nums[i] += converted[i]
        
        return nums