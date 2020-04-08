class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0 
        maximum = -999999999999
        for i in range(len(nums)):
            s = max(s+nums[i],nums[i])
            if s > maximum :
                maximum = s 
        return maximum
            
        