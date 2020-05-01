class Solution:
    def solve(self, nums):
        # Write your code here
        
        
        nums = [n*n for n in nums]
        nums = sorted(nums)
        return nums
