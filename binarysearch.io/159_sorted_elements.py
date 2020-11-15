class Solution:
    def solve(self, nums):
        nums2 = sorted(nums)
        ans = 0
        for i in range(len(nums)):
            if nums[i] == nums2[i]:
                ans += 1 
        return ans