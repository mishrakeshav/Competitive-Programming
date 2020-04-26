class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = dict()
        for i in range(len(nums)):
            
            if target - nums[i] in n:
                return [n[target-nums[i]],i]
            if nums[i] not in n:
                n[nums[i]] = i
                
            
                
        