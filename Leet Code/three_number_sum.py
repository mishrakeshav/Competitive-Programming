class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    l.extend([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    j -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    i += 1
        return l
