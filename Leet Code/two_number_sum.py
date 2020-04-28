class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = dict()
        for i in range(len(nums)):

            if target - nums[i] in n:
                return [n[target - nums[i]], i]
            if nums[i] not in n:
                n[nums[i]] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums = sorted(nums)
        i = 0
        j = n - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return True
            elif nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
        return False
