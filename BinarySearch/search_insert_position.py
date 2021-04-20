"""
link : https://leetcode.com/problems/search-insert-position/
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def condition(val):
            return target <= nums[val]
        left , right = 0,len(nums)
        while left < right:
            mid = (left + right)//2 
            if condition(mid):
                right = mid 
            else:
                left = mid + 1 
        return left 
        