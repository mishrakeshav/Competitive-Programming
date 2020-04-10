class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        next = 0
        for i in nums:
            if i != 0:
                nums[next] = i 
                next += 1 
        for i in range(next,len(nums)):
            nums[i] = 0
            
        