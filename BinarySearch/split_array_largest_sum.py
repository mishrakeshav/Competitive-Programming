"""
link : https://leetcode.com/problems/split-array-largest-sum/
"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def condition(val)->bool:
            c = 0
            k = 1 
            for i in nums:
                c += i 
                if c > val:
                    c = i 
                    k += 1 
            return k <= m
        
        right = sum(nums)
        left = max(nums) 
        while left < right:
            mid = (left + right)//2 
            if condition(mid):
                right = mid 
            else:
                left = mid + 1 