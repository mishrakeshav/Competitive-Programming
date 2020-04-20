class Solution:
    def solve(self, nums):
        n = len(nums)
        if n%2:
            return nums[n//2]
        else:
            return nums[n//2 - 1]

        
