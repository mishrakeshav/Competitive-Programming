class Solution:
    def solve(self, nums):
        if not nums:
            return nums
        nums.sort()
        n = len(nums)
        interval = []
        low = nums[0]
        for i in range(1,n):
            if nums[i-1]+1 != nums[i]:
                interval.append([low, nums[i-1]])
                low = nums[i]
        interval.append([low,nums[-1]])
        return interval