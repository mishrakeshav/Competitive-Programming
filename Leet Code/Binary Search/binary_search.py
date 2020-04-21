class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1
        while start <= end :
            mid = (start+end)//2 
            if nums[mid] == target:
                return mid 
            elif target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
        return - 1
        