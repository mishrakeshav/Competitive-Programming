class Solution:
    def solve(self, nums):
        # Write your code here
        for i in range(len(nums)):
            nums[i] += i
        return nums
