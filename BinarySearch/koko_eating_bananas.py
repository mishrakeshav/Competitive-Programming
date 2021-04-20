"""
link : https://leetcode.com/problems/koko-eating-bananas/
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(val):
            hr = 0 
            for i in piles:
                hr += (val + i - 1)//val
            return hr <= h 
        
        left,right = 1,max(piles)
        while left < right:
            mid = (left + right)//2 
            if condition(mid):
                right = mid 
            else:
                left = mid + 1 
        
        return left 
        