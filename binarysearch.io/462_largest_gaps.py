class Solution:
    def solve(self, nums):
        nums.sort()
        ans = 0 
        for i in range(1,len(nums)):
            ans = max(nums[i]-nums[i-1],ans)
        return ans