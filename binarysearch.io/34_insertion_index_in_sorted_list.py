class Solution:
    def solve(self, nums, target):
        left, right = 0, len(nums) - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if target >= nums[mid]:
                ans = mid + 1
                left = mid + 1
            else:
                right = mid - 1
        return ans